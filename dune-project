(lang dune 3.4)

(name prolog_interpreter)

 (using menhir 2.1)

(generate_opam_files true)

(source
 (github Em-Wright/parallel-prolog-interpreter))

(authors "Adam J. Stewart")

(license LICENSE)

(documentation https://github.com/Em-Wright/parallel-prolog-interpreter/blob/worker-parallel/README.md)

(package
 (name prolog_interpreter)
 (synopsis "A parallel prolog interpreter in OCaml")
 (description "A parallel (and sequential) Prolog interpreter written using the OCaml rpc_parallel library. ")
 (depends async ocaml dune core menhir ounit2 rpc_parallel)
 (tags
  ("prolog interpreter" prolog ocaml)))

; See the complete stanza docs at https://dune.readthedocs.io/en/stable/dune-files.html#dune-project
