# Benchmarking

Benchmarks live outside the `algorithms` package so the reusable library stays
lightweight. They are development tools for checking whether implementations
roughly match their expected time and space complexity.

## Install Benchmark Dependencies

```bash
python -m pip install -e ".[bench]"
```

The benchmark extra installs plotting support. The benchmark runner itself uses
the standard library for timing, memory tracking, CSV, and JSON output.

## Run a Suite

```bash
python -m benchmarks.cli benchmarks.benchmark_sorting
```

The sorting suite includes a Python `sorted` baseline so you can verify plotting
before your own sorting implementations exist.

Results are written to `benchmark-results/<suite-name>/`:

- `measurements.csv` contains every repeat.
- `summary.csv` contains aggregated values by input size.
- `summary.json` contains the same aggregated data for other tools.
- `plots/` contains PNG graphs.

Use `--no-plots` when you only need CSV and JSON:

```bash
python -m benchmarks.cli benchmarks.benchmark_sorting --no-plots
```

## Add a Benchmark

Each benchmark is a `BenchmarkCase`:

```python
from benchmarks.cases import BenchmarkCase, BenchmarkSuite, powers_of_two
from benchmarks.complexity import LINEAR, LINEARITHMIC
from algorithms.sorting import merge_sort


def random_ints(size: int) -> list[int]:
    ...


SUITE = BenchmarkSuite(
    name="sorting",
    cases=(
        BenchmarkCase(
            name="merge_sort random integers",
            input_factory=random_ints,
            operation=lambda values: merge_sort(values),
            sizes=powers_of_two(32, 4096),
            expected_time=LINEARITHMIC,
            expected_space=LINEAR,
        ),
    ),
)
```

Input factories should create fresh inputs for each repeat. This matters for
in-place algorithms and mutable data structures.

## Complexity Curves

The plotting layer overlays observed measurements with an expected curve such as
`O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n^2)`, or `O(n^3)`.

The expected curve is normalized to the final non-zero observation. The graph is
therefore a shape comparison, not a proof. It helps catch obvious mismatches,
such as a supposedly linear operation bending upward like a quadratic curve.

## Time and Space Measurement

The runner uses:

- `time.perf_counter()` for elapsed time.
- `tracemalloc` for peak Python memory allocated during the operation.
- repeated runs with a short warmup phase.

Memory measurements are useful for relative comparison, but they do not include
every byte held by the Python interpreter or native extensions.

## Suggested Benchmark Strategy

- Keep correctness tests separate from benchmarks.
- Benchmark operations independently where possible, such as insert, lookup,
  delete, heapify, extract-min, sort, search, or traversal.
- Choose input shapes that match the complexity claim. For graph algorithms,
  state whether the graph is sparse or dense.
- Use smaller maximum sizes for quadratic and cubic algorithms.
- Do not tune implementations only to win a benchmark. The project prioritizes
  correctness, readability, and educational clarity.
