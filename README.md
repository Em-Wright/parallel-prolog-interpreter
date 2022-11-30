# prolog

An implementation of Prolog written in OCaml

## Dependencies

This project depends on the following OCaml libraries:

* [OCamlfind](https://opam.ocaml.org/packages/ocamlfind/) for finding dependent libraries
* [Dune](https://opam.ocaml.org/packages/dune/) for building the project
* [OUnit](https://opam.ocaml.org/packages/ounit/) for unit testing
* [Menhir](https://opam.ocaml.org/packages/menhir/) for parser generation


The recommended way to install these dependencies is with [OPAM](https://opam.ocaml.org/):

```
$ opam install ocamlfind
$ opam install dune
$ opam install oUnit
$ opam install menhir
```

## Installation

To build this project, simply clone the repository and run `dune build`:

Afterwards, the interpreter can be run using one of the following:

```
$ ./bin/sequential.exe sequential -file myprologfile
$ ./bin/sequential.exe stack -file myprologfile
$ ./bin/parallel.exe -file myprologfile -num-workers 8

```

## Testing

To run the test-suite, simply run `dune test`:

```
$ dune test
```
