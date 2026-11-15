# Agency Poem — make.fun `agency-poem-01`

A program that writes one poem about agency to `/output/entry.txt`.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The poem is a fixed string in `main.py` (Python 3.13, standard library
only): 15 lines, 536 characters, no trailing newline. Two runs write
byte-identical output (sha256
`54559a8b367d3d15ca6828b17bb7c3b25ba428cda651edc935da18760557a428`).

License: MIT (see `LICENSE`).
