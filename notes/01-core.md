# Find a shortest unweighted path: implementation

## What the example does

Breadth-first search visits nodes by edge distance. Mark nodes when enqueuing to avoid cycles; the result is shortest only for unweighted edges.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "graph": {
    "a": [
      "b",
      "c"
    ],
    "b": [
      "d"
    ],
    "c": [
      "d"
    ]
  },
  "start": "a",
  "goal": "d"
}
```

Expected result:

```json
[
  "a",
  "b",
  "d"
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
