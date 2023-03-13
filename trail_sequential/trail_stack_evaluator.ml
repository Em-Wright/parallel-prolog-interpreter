open Core
open Include
open Trail_util

let rec eval_inner (q : Job.t Deque.t) db results =
  match (Deque.dequeue_back q) with
  | None -> results
  | Some job -> (
      match job.goals with
      | [] -> let soln = realise_solution job.var_mapping in
        eval_inner q db (soln::results)
      | g1::gl -> (
          (
            match !g1 with
            (* if goal is the true predicate *)
            | Exp.TermExp("true", []) -> Deque.enqueue_back q {goals=gl;var_mapping=job.var_mapping}
            | TermExp("equals", [lhs; rhs]) ->
              (* check if the lhs and rhs can unify *)
              let trail = Trail.create () in
              if (unify lhs rhs trail) then (
                Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
              ) else Trail.undo trail
            | TermExp("not_equal", [lhs;rhs]) -> (
                (* check if the lhs and rhs can unify. If they can, this is not a
                   successful substitution. If they don't, we can continue solving the
                   rest of the goals
                *)
                let trail = Trail.create () in
                if not (unify lhs rhs trail) then (
                  Trail.undo trail;
                  Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                ) else Trail.undo trail
              )
            | TermExp("greater_than", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 > i2 then
                    Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                | _ -> () (* arguments insufficiently instantiated *)
              )
            | TermExp("greater_than_or_eq", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 >= i2 then
                    Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                | _ -> () (* arguments insufficiently instantiated *)
              )
            | TermExp("less_than", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 < i2 then
                    Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                | _ -> () (* arguments insufficiently instantiated *)
              )
            | TermExp("less_than_or_eq", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 <= i2 then
                    Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                | _ -> () (* arguments insufficiently instantiated *)
              )
            | TermExp("is", [lhs; rhs]) -> (
                (* evaluate the arithmetic expressions with current substitutions, then check if it is
                   possible to unify them with any additional substitutions *)
                match !rhs with
                | ArithmeticExp (op, t1, t2) -> (
                    match (resolve_arith t1), (resolve_arith t2) with
                    | ArithmeticInt i1, ArithmeticInt i2 -> (
                        let result = perform_arithmetic op i1 i2 in
                        (
                          match !lhs with
                          | VarExp _ -> let trail = Trail.create () in
                            if unify lhs (ref (Exp.IntExp result)) trail then
                              Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                            else Trail.undo trail
                          | IntExp i -> if i = result then
                              Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                          | _ -> ()
                        )
                      )
                    | _ -> ()
                  )
                | IntExp result -> (
                    (
                      match !lhs with
                      | VarExp _ -> let trail = Trail.create () in
                        if unify lhs (ref (Exp.IntExp result)) trail then
                          Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping }
                        else Trail.undo trail
                      | IntExp i -> if i = result then
                          Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                      | _ -> ()
                    )
                  )
                | _ -> ()
              )
            | TermExp(_,_) -> (
                let db_copy = List.map db ~f:(fun clause ->
                    Clause.copy clause ) in
                let rec loop db_copy =
                  match db_copy with
                  | [] -> ()
                  | c::dbs -> (
                      let (head, body) = Clause.copy c in
                      let trail = Trail.create () in
                      if unify head g1 trail then (
                        let new_job = Job.deep_copy {goals=(body@gl); var_mapping=job.var_mapping} in
                        Deque.enqueue_back q new_job
                      ) ;
                      Trail.undo trail;
                      loop dbs
                    )
                in
                loop db_copy )
            | _ -> ()
          );
          eval_inner q db results
        )
    )


let command =
  Command.basic
    ~summary:"Sequential Prolog interpreter using a unification by assignment"
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
              (* NOTE we create an empty var_mapping here so we don't have overlap between the rules and the
              query *)
              let var_mapping = String.Table.create () in
              let b_converted : Exp.t ref list = List.map b ~f:(fun e -> convert e var_mapping |> ref ) in
              let q = Deque.create () in
              Deque.enqueue_front q ({goals=b_converted; var_mapping} : Job.t);
              let res = eval_inner q db_converted [] in
              List.iter res ~f:(fun result ->
                  print_endline "===============";
                  List.iter result ~f:(fun (a,b) ->
                      print_endline (a ^ " = "^b)
                    );
                  print_endline "===============";
                ); []
            )
    ]
