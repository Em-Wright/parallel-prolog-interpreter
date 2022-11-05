(lang dune 3.4)

(name prolog_interpreter)

 (using menhir 2.1)

(generate_opam_files true)

(source
 (github adamjstewart/prolog))

(authors "Adam J. Stewart")

(maintainers "Adam J. Stewart")

(license LICENSE)

(documentation https://url/to/documentation)

(package
 (name prolog_interpreter)
 (synopsis "A prolog interpreter in OCaml")
 (description "A longer description")
 (depends async ocaml dune core menhir ounit2 rpc_parallel)
 (tags
  ("prolog interpreter" prolog ocaml)))

; See the complete stanza docs at https://dune.readthedocs.io/en/stable/dune-files.html#dune-project
