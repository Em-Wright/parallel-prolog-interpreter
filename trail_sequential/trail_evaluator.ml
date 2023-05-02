open Core
open Include
open Trail_util


let rec eval_query q db (trail : Trail.t) var_mapping =
  match q with
  | [] -> let var_mapping_list = Hashtbl.to_alist var_mapping in
       [List.map var_mapping_list ~f:(fun (a,b) -> ((VarExp a, convert_back (VarExp (ref b))) : Ast.exp * Ast.exp) ) ], []
  | (g1, depth)::gl ->
      (
        match !g1 with
        (* if goal is the true predicate *)
        | Exp.TermExp("true", []) -> eval_query gl db trail var_mapping
        | TermExp("cut", []) -> let res, cut = eval_query gl db trail var_mapping in
          (res, (depth-1)::cut)
        | TermExp("equals", [lhs; rhs]) -> (
            (* check if the lhs and rhs can unify *)
            let t = Trail.mark trail in
            let res =
              if unify lhs rhs trail then
                eval_query gl db trail var_mapping
              else ([], [])
            in
            Trail.undo trail t;
            res
          )
        | TermExp("not_equal", [lhs;rhs]) -> (
            (* check if the lhs and rhs can unify. If they can, this is not a
               successful substitution. If they don't, we can continue solving the
               rest of the goals
            *)
            let t = Trail.mark trail in
            let res =
              if not (unify lhs rhs trail) then (
                Trail.undo trail t;
                eval_query gl db trail var_mapping;
              ) else ([], [])
            in
            Trail.undo trail t;
            res
          )
        | TermExp("greater_than", [lhs; rhs]) -> (
          match (Exp.resolve !lhs), (Exp.resolve !rhs) with
          | IntExp i1, IntExp i2 ->
            if i1 > i2 then
              eval_query gl db trail var_mapping
            else [], []
          | _ -> [], [] (* arguments insufficiently instantiated *)
        )
        | TermExp("greater_than_or_eq", [lhs; rhs]) -> (
            match (Exp.resolve !lhs), (Exp.resolve !rhs) with
            | IntExp i1, IntExp i2 ->
              if i1 >= i2 then
                eval_query gl db trail var_mapping
              else [], []
            | _ -> [], [] (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than", [lhs; rhs]) -> (
            match (Exp.resolve !lhs), (Exp.resolve !rhs) with
            | IntExp i1, IntExp i2 ->
              if i1 < i2 then
                eval_query gl db trail var_mapping
              else [], []
            | _ -> [], [] (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than_or_eq", [lhs; rhs]) -> (
            match (Exp.resolve !lhs), (Exp.resolve !rhs) with
            | IntExp i1, IntExp i2 ->
              if i1 <= i2 then
                eval_query gl db trail var_mapping
              else [], []
            | _ -> [], [] (* arguments insufficiently instantiated *)
          )
        | TermExp("is", [lhs; rhs]) -> (
            (* evaluate the arithmetic expressions with current substitutions, then check if it is
               possible to unify them with any additional substitutions *)
            match !rhs with
            | ArithmeticExp (op, t1, t2) -> (
                match (resolve_arith t1), (resolve_arith t2) with
                | ArithmeticInt i1, ArithmeticInt i2 -> (
                    let result = perform_arithmetic op i1 i2 in
                    let t = Trail.mark trail in
                    let res =
                    (
                      match !lhs with
                      | VarExp _ -> if unify lhs (ref (Exp.IntExp result)) trail then
                          eval_query gl db trail var_mapping else [], []
                      | IntExp i -> if i = result then eval_query gl db trail var_mapping else [], []
                      | _ -> [], []
                    ) in Trail.undo trail t; res
                  )
                | _ -> [], []
              )
            | IntExp result -> (
                let t = Trail.mark trail in
                 let res = (
                  match !lhs with
                  | VarExp _ -> if unify lhs (ref (Exp.IntExp result)) trail then
                      eval_query gl db trail var_mapping else [], []
                  | IntExp i -> if i = result then eval_query gl db trail var_mapping else [], []
                  | _ -> [], []
                )
                in Trail.undo trail t; res
              )
            | _ -> [], []
          )
        | TermExp(_,_) -> (
            let db_copy = List.map db ~f:(fun clause -> Clause.copy clause trail) in
            let rec loop db_copy (res, acc_cuts) =
              match db_copy with
              | [] -> (res, acc_cuts)
              | c::dbs -> (let t = Trail.mark trail in
                           let (head, body) = Clause.copy c trail in
                           Trail.undo trail t;
                           let res2, cut =
                             if unify head g1 trail then (
                               let body2 = List.zip_exn body (List.init (List.length body) ~f:(fun _ -> (depth+1))) in
                               eval_query (body2@gl) db trail var_mapping
                             ) else [], [] in
                           Trail.undo trail t;
                           (
                             match cut with
                             | d::cuts -> if Int.equal d depth then (res2 @ res, cuts@acc_cuts)
                               else (
                                 if d > depth then print_endline "something has gone terribly wrong";
                                 loop dbs (res2 @ res, cut@acc_cuts))
                             | [] -> loop dbs(res2 @ res, acc_cuts)
                           )
                          )
            in
            loop db_copy ([],[]) )
        | _ -> eval_query gl db trail var_mapping
      )



let command =
  Command.basic
    ~summary:"Sequential Prolog interpreter using a trail stack"
    [%map_open.Command
      let filename =
        flag
          ~doc:"FILE to read prolog from"
          "file"
          (required string)
      in
      fun () ->
        Interface.main filename
          ~eval_function:(fun db b ->
              (* convert the db and b into the required formats then feed to the eval function *)
              let db_converted : Clause.t list = List.map db
                  ~f:(fun dec ->
                      let var_mapping = String.Table.create () in
                      match dec with
                      | Clause (h, b) -> let h2 = convert h var_mapping in
                        let b2 = List.map b ~f:(fun e -> convert e var_mapping |> ref) in
                        (ref h2, b2)
                      | Query _ -> Error.raise (Error.of_string "There should be no queries in the database")
                    )
              in
              let var_mapping = String.Table.create () in
              let b_converted : (Exp.t ref * int) list = List.map b ~f:(fun e -> convert e var_mapping |> ref , 0) in
              let trail = Stack.create () in
              let res, _ = eval_query b_converted db_converted trail var_mapping in
              res
            )
    ]
