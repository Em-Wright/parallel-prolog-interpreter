%{
    open Ast

    (* The fact:
           Head.
       is equivalent to the rule:
           Head :- true.
    *)
    let fact_sugar p =
        Clause (
            p,
            [TermExp ("true", [])]
        )

    (* An atom can be regarded as a compound term with arity zero *)
    let atom_sugar a =
        TermExp (
            a,
            []
        )
%}

/* Refer to:

   https://www.cs.uni-potsdam.de/wv/lehre/Material/Prolog/Eclipse-Doc/userman/node140.html
   https://github.com/simonkrenger/ch.bfh.bti7064.w2013.PrologParser/blob/master/doc/prolog-bnf-grammar.txt

   for a description of the grammar */

/* Tokens */

/* Constants */
%token <int> INT
%token <string> ATOM

/* Variables */
%token <string> VAR

/* Symbols */
%token RULE       /* :- */
%token QUERY      /* ?- */
%token PERIOD     /* .  */
%token LPAREN     /* (  */
%token RPAREN     /* )  */
%token LBRACKET   /* [  */
%token RBRACKET   /* ]  */
%token PIPE
%token COMMA      /* ,  */
%token PLUS
%token MINUS
%token MULT
%token DIV
%token IS
%token EQUALS
%token NOTEQUAL
%token GT
%token LT
%token GEQ
%token LEQ
%token CUT

/* Meta-characters */
%token EOF

/* Start symbols */
%start clause

/* Types */
%type <Ast.dec> clause
%type <Ast.exp> predicate term structure
%type <Ast.exp list> term_list predicate_list
%type <Ast.arithmetic_operand> arithmetic_operand

%%

clause:
    | p = predicate; PERIOD                             { fact_sugar p }
    | p = predicate; RULE; pl = predicate_list; PERIOD  { Clause (p, pl) }
    | QUERY; pl = predicate_list; PERIOD                { Query pl }

predicate_list:
    | p = predicate                                     { [p] }
    | p = predicate; COMMA; pl = predicate_list         { p :: pl }

predicate:
    | a = ATOM                                          { atom_sugar a }
    | s = structure                                     { s }

structure:
    | a = ATOM; LPAREN; RPAREN                          { atom_sugar a }
    | a = ATOM; LPAREN; tl = term_list; RPAREN          { TermExp (a, tl) }
    | v = VAR; IS; a = arithmetic                       { TermExp ("is", [VarExp v; a]) }
    | t1 = comparable; EQUALS; t2 = comparable          { TermExp ("equals", [t1; t2]) }
    | t1 = comparable; NOTEQUAL; t2 = comparable        { TermExp ("not_equal", [t1; t2]) }
    | t1 = comparable; GT; t2 = comparable              { TermExp ("greater_than", [t1; t2]) }
    | t1 = comparable; LT; t2 = comparable              { TermExp ("less_than", [t1; t2]) }
    | t1 = comparable; GEQ; t2 = comparable             { TermExp ("greater_than_or_eq", [t1; t2]) }
    | t1 = comparable; LEQ; t2 = comparable             { TermExp ("less_than_or_eq", [t1; t2]) }
    | CUT                                               { TermExp ("cut", []) }

list:
    | LBRACKET; RBRACKET                                { TermExp ("empty_list", [])}
    | LBRACKET; l = list_body; RBRACKET                 { l }

list_body:
    | t = term                                          { TermExp("list", [t; TermExp("empty_list", [])]) }
    | t = term; COMMA; l = list_body                    { TermExp("list", [t; l]) }
    | t = term; PIPE; tl = term                         { TermExp("list", [t; tl]) }

term_list:
    | t = term                                          { [t] }
    | t = term; COMMA; tl = term_list                   { t :: tl }

term:
    | a = ATOM                                          { atom_sugar a }
    | s = structure                                     { s }
    | a = arithmetic                                    { a }
    | c = comparable                                    { c }
    | l = list                                          { l }

comparable:
    | i = INT { IntExp i }
    | v = VAR { VarExp v }

arithmetic:
    | a1 = arithmetic_operand; PLUS; a2 = arithmetic_operand { ArithmeticExp (PLUS, a1, a2)}
    | a1 = arithmetic_operand; MINUS; a2 = arithmetic_operand { ArithmeticExp (MINUS, a1, a2)}
    | a1 = arithmetic_operand; MULT; a2 = arithmetic_operand { ArithmeticExp (MULT, a1, a2)}
    | a1 = arithmetic_operand; DIV; a2 = arithmetic_operand { ArithmeticExp (DIV, a1, a2)}

arithmetic_operand:
    | i = INT                                           { ArithmeticInt i}
    | v = VAR                                           { ArithmeticVar v}
