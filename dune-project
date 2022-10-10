(lang dune 3.4)

(name sequential_interpreter)

 (using menhir 2.1)

(generate_opam_files true)

(source
 (github adamjstewart/prolog))

(authors "Adam J. Stewart")

(maintainers "Adam J. Stewart")

(license LICENSE)

(documentation https://url/to/documentation)

(package
 (name sequential_interpreter)
 (synopsis "A sequential prolog interpreter")
 (description "A longer description")
 (depends ocaml dune core menhir ounit2)
 (tags
  ("prolog interpreter" prolog)))

; See the complete stanza docs at https://dune.readthedocs.io/en/stable/dune-files.html#dune-project
