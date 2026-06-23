<div align="center">
  <img src="docs/assets/logo.png" alt="Algorithms in Python logo" width="120" height="120" />

  <h1>Algorithms in Python</h1>

  <p>
    <strong>
      Typed, tested, and documented Python implementations of algorithms and data structures from scratch.
    </strong>
  </p>

  <p>
    Built for algorithm revision, interview preparation, long-term reference, and future reuse in visualisation tools.
  </p>

  <p>
    <a href="https://github.com/mezza/algorithms/actions/workflows/ci.yml">
      <img src="https://github.com/mezza/algorithms/actions/workflows/ci.yml/badge.svg" alt="CI status" />
    </a>
    <img src="https://img.shields.io/badge/python-3.11%2B-blue" alt="Python 3.11+" />
    <img src="https://img.shields.io/badge/typed-mypy-blue" alt="Typed with mypy" />
    <img src="https://img.shields.io/badge/style-ruff-black" alt="Code style: Ruff" />
    <img src="https://img.shields.io/badge/tests-pytest-green" alt="Tests: pytest" />
    <img src="https://img.shields.io/badge/license-MIT-blue" alt="License: MIT" />
  </p>
</div>

---

## Overview

**Algorithms in Python** is a reusable Python package containing implementations of core algorithms and data structures from scratch.

This project is designed for:

- algorithm and data structures revision
- LeetCode-style interview preparation
- long-term computer science reference
- clean package design practice
- future reuse in algorithm visualisation tools

The goal is not only to implement algorithms, but to build a clean, reusable package that demonstrates correctness, clarity, documentation, testing, and maintainable software design.

---

## Project Status

This project is in active development.

Current focus:

* Package structure
* Testing and documentation standards
* Foundational searching and sorting algorithms
* Abstract data type contracts
* Visualisation-friendly tracing API design

Next recommended implementation:

* [ ] Selection Sort

---

## Features

* Implementations from scratch
* Typed Python code
* Public package APIs
* Abstract data type contracts
* Multiple concrete implementations where useful
* Unit tests for correctness
* Reusable contract tests for ADTs
* Complexity analysis for each algorithm
* Edge case documentation
* Optional tracing APIs for future visualisation
* Clean separation between algorithm logic and demos/UI code
* Written for readability and learning, not code golf

---

## Motivation

This project began as a way to revisit the algorithms and data structures I studied at university. It has since grown into a reusable Python package designed around clean APIs, correctness, testing, documentation, and future visualisation support.

The goal is to make each implementation understandable enough to learn from, but structured enough to reuse in other projects.

Possible future projects that could depend on this package include:

* a data structures and algorithms visualiser website
* a teaching tool for algorithm traces
* an API that returns algorithm execution steps
* interactive notebooks for revision
* small demo applications for algorithm concepts

---

## Design Priorities

The implementations prioritize:

1. correctness
2. readability
3. educational clarity
4. testability
5. reusable APIs
6. type safety
7. documentation quality
8. visualisation readiness where appropriate

These implementations do not aim to outperform Python's built-in data structures or standard library algorithms.

For example, Python's `list.sort()` and `sorted()` are highly optimized production implementations. This package implements algorithms manually so their behavior, trade-offs, and internal mechanics are clear.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/LucaMezz/algorithms.git
cd algorithms
```

Install the package in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

After installation, modules can be imported from the `algorithms` package.

---

## Usage

Example usage:

```python
from algorithms.searching import binary_search
from algorithms.sorting import merge_sort

values = [5, 3, 1, 4, 2]

sorted_values = merge_sort(values)
index = binary_search(sorted_values, 4)

print(sorted_values)
print(index)
```

Example data structure usage:

```python
from algorithms.data_structures import ArrayStack

stack = ArrayStack[int]()
stack.push(10)
stack.push(20)

assert stack.pop() == 20
assert stack.pop() == 10
```

Example tracing usage for future visualisation:

```python
from algorithms.sorting import trace_selection_sort

for event in trace_selection_sort([3, 1, 2]):
    print(event)
```

The normal algorithm API should return the final result. Tracing APIs should expose intermediate states without mixing visualisation-specific logic into the core implementation.

---

## Package Goals

This repository should be designed as an installable Python package, not just a collection of standalone scripts.

That means implementations should be:

* importable from other Python code
* tested as package modules
* documented with stable public APIs
* separated from command-line, visualisation, or demo-specific code
* designed so future projects can reuse the algorithms directly

A future visualiser website, desktop app, or API should be able to depend on this package without copying the implementation code.

---

## Suggested Repository Structure

```text
algorithms-python/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── pyproject.toml
├── .gitignore
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── algorithm_request.md
│   │   └── documentation_improvement.md
│   └── pull_request_template.md
├── src/
│   └── algorithms/
│       ├── __init__.py
│       ├── py.typed
│       ├── adts/
│       │   ├── __init__.py
│       │   ├── stack.py
│       │   ├── queue.py
│       │   ├── deque.py
│       │   ├── priority_queue.py
│       │   ├── dictionary.py
│       │   ├── set.py
│       │   └── sequence.py
│       ├── data_structures/
│       │   ├── __init__.py
│       │   ├── arrays/
│       │   ├── linked_lists/
│       │   ├── stacks/
│       │   ├── queues/
│       │   ├── heaps/
│       │   ├── hash_tables/
│       │   ├── trees/
│       │   └── union_find/
│       ├── searching/
│       │   └── __init__.py
│       ├── sorting/
│       │   └── __init__.py
│       ├── selection/
│       │   └── __init__.py
│       ├── graphs/
│       │   └── __init__.py
│       ├── greedy/
│       │   └── __init__.py
│       ├── dynamic_programming/
│       │   └── __init__.py
│       ├── shortest_paths/
│       │   └── __init__.py
│       ├── flows/
│       │   └── __init__.py
│       ├── strings/
│       │   └── __init__.py
│       ├── compression/
│       │   └── __init__.py
│       └── tracing/
│           └── __init__.py
├── tests/
│   ├── adts/
│   ├── data_structures/
│   ├── searching/
│   ├── sorting/
│   ├── graphs/
│   ├── dynamic_programming/
│   └── strings/
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   ├── adts/
│   ├── api/
│   ├── notes/
│   ├── traces/
│   ├── decisions/
│   │   ├── 0001-use-src-layout.md
│   │   ├── 0002-separate-adts-from-implementations.md
│   │   └── 0003-add-tracing-apis-for-visualisation.md
│   └── complexity-cheatsheet.md
├── examples/
│   ├── sorting/
│   ├── graphs/
│   ├── data_structures/
│   └── tracing/
└── benchmarks/
    ├── benchmark_sorting.py
    ├── benchmark_hash_tables.py
    └── benchmark_graphs.py
```

Recommended convention for each algorithm:

```text
src/algorithms/<topic>/<algorithm_name>.py
tests/<topic>/test_<algorithm_name>.py
docs/notes/<algorithm_name>.md
```

Example:

```text
src/algorithms/sorting/merge_sort.py
tests/sorting/test_merge_sort.py
docs/notes/merge_sort.md
```

---

## Package Design Requirements

Because this repository may be reused by future projects, implementation files should be designed as library code.

### Public API

Each package folder should expose stable public imports through `__init__.py` files.

Example:

```python
from algorithms.sorting.merge_sort import merge_sort

__all__ = ["merge_sort"]
```

This allows users to import from a clean package path:

```python
from algorithms.sorting import merge_sort
```

Avoid forcing future projects to import from deeply nested internal files unless necessary.

### Internal vs Public Code

Use naming conventions to separate public API from internal helpers.

Public examples:

```python
merge_sort
ArrayStack
BinaryHeapPriorityQueue
breadth_first_search
```

Internal examples:

```python
_merge
_partition
_sift_down
_reconstruct_path
```

Internal helpers can change freely. Public functions and classes should be more stable.

### No Side Effects on Import

Modules should not run demos, print output, read files, or execute algorithm examples when imported.

Good:

```python
def merge_sort(values: Sequence[int]) -> list[int]:
    ...
```

Avoid:

```python
print(merge_sort([3, 2, 1]))
```

Demo code should go in tests, docs, examples, or explicit scripts, not inside package modules.

### Dependency Rule

Keep the core package lightweight.

The main algorithm package should avoid heavy runtime dependencies. Most algorithms should only need the Python standard library.

Development dependencies such as test runners, type checkers, linters, documentation tools, and benchmark tools should stay separate from runtime dependencies.

### Typed Package Marker

The package should include `py.typed` so downstream users and type checkers know the package provides type information.

```text
src/algorithms/py.typed
```

---

## Visualisation-Friendly Design

This package may eventually be used by a data structures and algorithms visualiser. The package should therefore be designed so algorithms can optionally expose step-by-step execution data.

The core algorithm implementation should remain simple and focused.

Good:

```python
merge_sort(values)
trace_merge_sort(values)
```

Also acceptable for some algorithms:

```python
merge_sort(values, tracer=tracer)
```

Avoid making the normal algorithm depend on UI concerns, JSON formats, animations, web-specific concepts, or rendering libraries.

The package should not know whether the caller is:

* a command-line tool
* a website
* a desktop app
* a test suite
* a notebook
* an API server

It should expose clean algorithmic behavior and optional structured tracing data.

### Structured Trace Events

Tracing functions should yield structured events rather than printing text.

Example:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class CompareEvent:
    left_index: int
    right_index: int


@dataclass(frozen=True)
class SwapEvent:
    first_index: int
    second_index: int
```

A tracing function can then yield events:

```python
from collections.abc import Iterator, Sequence


def trace_selection_sort(values: Sequence[int]) -> Iterator[CompareEvent | SwapEvent]:
    ...
```

This makes it easier for a future visualiser to convert algorithm steps into animations.

---

## Abstract Data Type Requirements

For data structures, separate the abstract data type from the concrete implementation.

An abstract data type describes the public contract:

* what operations are supported
* what each operation means
* what each operation returns
* what errors or edge cases are expected
* what complexity guarantees the implementation aims to provide

A concrete implementation describes how that contract is implemented internally.

For example, a stack ADT can be implemented using:

* a dynamic array
* a singly linked list
* a doubly linked list

The external stack operations remain the same:

```python
push(value)
pop()
peek()
is_empty()
__len__()
```

But the internal representation can change.

### Recommended ADT Structure

Use Python protocols or abstract base classes to describe contracts where useful.

Example:

```python
from typing import Protocol, TypeVar

T = TypeVar("T")


class Stack(Protocol[T]):
    """Contract for last-in, first-out collections."""

    def push(self, value: T) -> None:
        """Add value to the top of the stack."""
        ...

    def pop(self) -> T:
        """Remove and return the top value from the stack."""
        ...

    def peek(self) -> T:
        """Return the top value without removing it."""
        ...

    def is_empty(self) -> bool:
        """Return True if the stack contains no values."""
        ...

    def __len__(self) -> int:
        """Return the number of values in the stack."""
        ...
```

Then implementations can satisfy the same contract:

```text
src/algorithms/adts/stack.py
src/algorithms/data_structures/stacks/array_stack.py
src/algorithms/data_structures/stacks/linked_stack.py
```

### ADTs to Define

Add contracts for common abstract data types:

* [ ] Sequence ADT
* [ ] Stack ADT
* [ ] Queue ADT
* [ ] Deque ADT
* [ ] Priority Queue ADT
* [ ] Dictionary / Map ADT
* [ ] Set ADT
* [ ] Disjoint Set / Union-Find ADT
* [ ] Graph ADT
* [ ] Tree ADT

### Example: Sequence ADT

A sequence is an ordered collection. It can be backed by different concrete structures, such as a contiguous dynamic array or a linked list.

Common operations:

```python
get(index)
set(index, value)
insert(index, value)
delete(index)
append(value)
prepend(value)
contains(value)
__len__()
```

Possible implementations:

* dynamic array
* singly linked list
* doubly linked list

Trade-offs:

| Operation               |  Dynamic Array |       Singly Linked List | Doubly Linked List |
| ----------------------- | -------------: | -----------------------: | -----------------: |
| Index access            |           O(1) |                     O(n) |               O(n) |
| Append                  | Amortized O(1) |   O(n) or O(1) with tail |     O(1) with tail |
| Prepend                 |           O(n) |                     O(1) |               O(1) |
| Insert after known node |            N/A |                     O(1) |               O(1) |
| Delete known node       |            N/A | O(n) if previous unknown |               O(1) |
| Search by value         |           O(n) |                     O(n) |               O(n) |

### Example: Priority Queue ADT

A priority queue can be implemented using several backing structures:

* unsorted array
* sorted array
* binary heap
* binomial heap
* Fibonacci heap

The contract remains similar:

```python
insert(item, priority)
peek_min()
extract_min()
decrease_key(item, new_priority)
is_empty()
__len__()
```

Different implementations have different complexity trade-offs:

| Operation    |     Unsorted Array |                   Sorted Array | Binary Heap |     Fibonacci Heap |
| ------------ | -----------------: | -----------------------------: | ----------: | -----------------: |
| Insert       |               O(1) |                           O(n) |    O(log n) |     Amortized O(1) |
| Peek min     |               O(n) |                           O(1) |        O(1) |               O(1) |
| Extract min  |               O(n) | O(1) or O(n), depending layout |    O(log n) | Amortized O(log n) |
| Decrease key | O(1) if item known |                           O(n) |    O(log n) |     Amortized O(1) |

This distinction is important because algorithms such as Dijkstra's algorithm, Prim's algorithm, heapsort, and event scheduling depend on priority queue behavior, not necessarily on one specific implementation.

### Implementation Rule

When implementing a data structure, document both:

1. The ADT contract: the operations and expected behavior.
2. The concrete implementation: the internal representation and complexity trade-offs.

For example:

```text
Stack ADT
├── ArrayStack
└── LinkedStack

Queue ADT
├── CircularArrayQueue
└── LinkedQueue

PriorityQueue ADT
├── UnsortedArrayPriorityQueue
├── BinaryHeapPriorityQueue
└── FibonacciHeapPriorityQueue

Map ADT
├── ChainedHashTable
├── OpenAddressedHashTable
└── BinarySearchTreeMap
```

### Testing Rule

Tests should be written against the ADT behavior first, then reused against multiple implementations.

For example, the same stack behavior tests should pass for both `ArrayStack` and `LinkedStack`.

```python
def stack_contract_tests(stack_factory):
    stack = stack_factory()

    assert stack.is_empty()

    stack.push(1)
    stack.push(2)

    assert len(stack) == 2
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()
```

This helps prove that each implementation satisfies the same abstract contract.

---

## Recommended Python Style

Prefer clear, readable implementations over clever micro-optimizations.

This repository is primarily for learning, revision, long-term reference, and reuse, so the code should be easy to read, explain, test, and modify.

### Type Annotations

All Python code should use type annotations.

Type annotations serve two purposes:

1. They make the code easier to understand.
2. They act as lightweight documentation for inputs, outputs, and internal data structures.

Functions should annotate parameters and return values:

```python
from collections.abc import Sequence


def binary_search(values: Sequence[int], target: int) -> int | None:
    ...
```

Classes should annotate important attributes:

```python
class ArrayStack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []
```

Avoid using `Any` unless there is a clear reason. Prefer generic type variables for reusable data structures.

```python
from typing import TypeVar

T = TypeVar("T")
```

### Docstrings

All public functions, classes, and methods should have docstrings.

Docstrings should explain:

* what the function or class does
* what the parameters mean when not obvious
* what is returned
* what errors may be raised
* any important assumptions
* the time and space complexity when useful

Example:

```python
from collections.abc import Sequence


def binary_search(values: Sequence[int], target: int) -> int | None:
    """Return the index of target in a sorted sequence, or None if absent.

    Args:
        values: A sequence sorted in non-decreasing order.
        target: The value to search for.

    Returns:
        The index of target if it exists, otherwise None.

    Time complexity:
        O(log n)

    Space complexity:
        O(1)
    """
    ...
```

For private helper functions, docstrings are optional if the function is small and obvious. If the helper contains non-trivial logic, it should still have a docstring.

### Self-Documenting Names

Functions, variables, classes, and modules should be named clearly enough that the code mostly explains itself.

Prefer names like:

```python
left_index
right_index
middle_index
current_node
parent_index
heap_size
visited_vertices
```

Avoid unclear names like:

```python
i
j
x
tmp
data
result
```

Short names are fine only when they are conventional and local:

* `i` for a small loop index
* `j` for a nested loop index
* `n` for input size
* `u` and `v` for graph vertices in edge-processing code

Even then, use clearer names when it improves readability.

### Inline Comments

Inline comments should explain why something is done, not merely repeat what the code says.

Good comments are useful for:

* loop invariants
* tricky index arithmetic
* recursive base cases
* graph traversal state
* dynamic programming recurrence choices
* heap rebalancing steps
* correctness reasoning
* non-obvious edge cases

Example:

```python
while left <= right:
    # The target, if present, must be inside values[left:right + 1].
    middle = (left + right) // 2
```

Avoid comments that only restate the code:

```python
# Increment i by 1.
i += 1
```

For larger chunks of code that are not immediately clear on their own, add a short comment before the block explaining the idea.

```python
# Restore the heap property by repeatedly swapping the new item with its parent
# until the parent is smaller or the item reaches the root.
while index > 0:
    ...
```

### Avoid Hidden Implementations

Avoid using Python standard library shortcuts that hide the algorithm you are trying to learn. For example:

* do not use `list.sort()` to implement sorting algorithms
* do not use `heapq` to implement your own heap
* do not use `bisect` to implement binary search
* do not use `networkx` for graph algorithms

Using these libraries for comparison tests is fine, but not for the main implementation.

### Code Quality Checklist

Before marking an implementation as complete, check that:

* [ ] all public functions have type annotations
* [ ] all public methods have type annotations
* [ ] all public classes have docstrings
* [ ] all public functions and methods have docstrings
* [ ] important internal attributes are annotated
* [ ] variable and function names are self-documenting where possible
* [ ] unclear logic has inline comments
* [ ] comments explain reasoning rather than restating code
* [ ] the implementation avoids shortcuts that hide the algorithm being learned

---

## Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=algorithms --cov-report=term-missing
```

Every completed algorithm should include tests for normal cases, edge cases, and where practical, randomized comparisons against a simple trusted implementation.

For each algorithm, include tests for:

* empty inputs
* single-element inputs
* duplicate values
* already sorted inputs
* reverse sorted inputs
* invalid inputs where relevant
* randomized small cases compared against a simple trusted implementation

Example for sorting algorithms:

```python
def test_sort_empty():
    assert merge_sort([]) == []


def test_sort_single_element():
    assert merge_sort([1]) == [1]


def test_sort_duplicates():
    assert merge_sort([3, 1, 2, 1]) == [1, 1, 2, 3]


def test_sort_reverse_order():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
```

For graph algorithms, test:

* disconnected graphs
* cycles
* self-loops where relevant
* multiple valid outputs
* unreachable vertices
* directed and undirected variants separately

For dynamic programming algorithms, test:

* base cases
* impossible cases
* multiple optimal solutions
* reconstruction correctness
* small brute-force comparisons where possible

For ADTs, write reusable contract tests and apply them to every implementation of the same contract.

---

## Code Quality

Run formatting:

```bash
ruff format .
```

Run linting:

```bash
ruff check .
```

Run type checking:

```bash
mypy src
```

Alternatively, this project may use Pyright instead of Mypy:

```bash
pyright
```

The final project should consistently run:

* formatting
* linting
* type checking
* tests
* coverage checks where useful

---

## Continuous Integration

The GitHub Actions CI pipeline should run on every push and pull request.

CI should check:

* package installation
* formatting
* linting
* type correctness
* unit tests
* coverage where useful

Recommended workflow path:

```text
.github/workflows/ci.yml
```

Once CI is configured, add a CI badge near the top of this README.

---

## Documentation

Each non-trivial algorithm should have a short note in `docs/notes`.

Suggested note template:

```md
# Algorithm Name

## Idea

Brief explanation of the algorithm.

## When to Use

Describe the situations where this algorithm is useful.

## Complexity

| Case | Time | Space |
|---|---:|---:|
| Best | | |
| Average | | |
| Worst | | |

## Edge Cases

- Empty input
- Single element input
- Duplicate values
- Already sorted input
- Reverse sorted input

## Implementation Notes

Important implementation details, invariants, or gotchas.

## Example

Small worked example.
```

Future documentation may be published as a docs site using a tool such as MkDocs Material, Sphinx, pdoc, or Docusaurus.

---

## Examples

Examples should live outside the package internals.

Possible structure:

```text
examples/
├── sorting/
│   └── merge_sort_example.py
├── graphs/
│   └── bfs_example.py
├── data_structures/
│   └── stack_example.py
└── tracing/
    └── selection_sort_trace_example.py
```

Examples should demonstrate public package APIs rather than importing private helpers.

---

## Benchmarks

Benchmarks are optional and should be added after the core package, tests, and documentation are established.

Possible structure:

```text
benchmarks/
├── benchmark_sorting.py
├── benchmark_hash_tables.py
└── benchmark_graphs.py
```

Potential benchmarks:

* custom merge sort vs Python `sorted`
* different priority queue implementations
* different hash table collision strategies
* Dijkstra's algorithm with different priority queue implementations
* recursive vs iterative graph traversal

Benchmarks should be used for learning and comparison, not as the main definition of project quality.

---

## Architecture Decisions

For important design choices, add short architecture decision records in `docs/decisions`.

Example decisions:

```text
docs/decisions/0001-use-src-layout.md
docs/decisions/0002-separate-adts-from-implementations.md
docs/decisions/0003-add-tracing-apis-for-visualisation.md
```

Example ADR format:

```md
# 0002 — Separate ADTs from Concrete Implementations

## Decision

Abstract data type contracts will be defined separately from concrete implementations.

## Reason

This allows multiple implementations to satisfy the same behavior while making performance trade-offs explicit.

## Consequences

Tests can be written against contracts and reused across implementations.
```

---

## Contributing

Contributions are welcome once the project structure is stable.

Each new algorithm or data structure should include:

* implementation
* tests
* type annotations
* docstrings
* complexity notes
* edge case coverage
* package export where appropriate
* documentation for non-trivial algorithms

Recommended files:

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/bug_report.md
.github/ISSUE_TEMPLATE/algorithm_request.md
.github/ISSUE_TEMPLATE/documentation_improvement.md
.github/pull_request_template.md
```

Suggested pull request checklist:

```md
## Summary

Describe the change.

## Checklist

- [ ] Implementation added
- [ ] Tests added
- [ ] Type annotations added
- [ ] Docstrings added
- [ ] Complexity documented
- [ ] README checklist updated
```

---

## Security

This project is an educational algorithms package and is not intended for security-critical use.

If you discover unsafe behavior, please open an issue or contact the maintainer.

Recommended file:

```text
SECURITY.md
```

---

## License

This project should include an open-source license.

Recommended options:

* MIT License
* Apache License 2.0

Recommended file:

```text
LICENSE
```

---

## Completion Criteria

An algorithm is only marked complete when it has:

* [ ] implementation
* [ ] tests
* [ ] type annotations
* [ ] docstrings
* [ ] complexity analysis
* [ ] edge case notes
* [ ] package export where appropriate
* [ ] documentation for non-trivial algorithms
* [ ] no hidden use of built-in shortcuts that replace the algorithm being learned

A data structure is only marked complete when it has:

* [ ] ADT contract where appropriate
* [ ] concrete implementation
* [ ] tests against expected behavior
* [ ] reusable contract tests where appropriate
* [ ] type annotations
* [ ] docstrings
* [ ] complexity analysis for operations
* [ ] edge case notes
* [ ] package export where appropriate

---

## Progress Summary

| Area                                  | Completed | Total |
| ------------------------------------- | --------: | ----: |
| Searching, Sorting, and Selection     |         0 |    28 |
| Graph Traversal and Connectivity      |         0 |    10 |
| Shortest Paths and Transitive Closure |         0 |     7 |
| Dynamic Programming                   |         0 |    12 |
| Flow and Matching                     |         0 |     4 |
| Hashing                               |         0 |     3 |
| Trees                                 |         0 |     8 |
| String Algorithms and Compression     |         1 |    13 |
| Practical Interview Extensions        |         0 |    61 |
| Total                                 |         1 |   152 |

---

## Implementation Roadmap

This roadmap keeps the original university algorithms first, because notes already exist for them. The additional practical interview and software-engineering algorithms are added afterwards as extension phases.

---

# Part 1 — Original University Algorithms

## Phase 1 — Foundations: Searching, Basic Sorting, and Recursion

These algorithms build the base skills needed for almost everything else: loops, invariants, recursion, divide-and-conquer, and basic complexity analysis.

* [ ] Binary Search
* [ ] Selection Sort
* [ ] Insertion Sort
* [ ] Karatsuba's Multiplication Algorithm
* [ ] Merge
* [ ] Merge Sort

Recommended order:

1. Selection Sort
2. Insertion Sort
3. Binary Search
4. Merge
5. Merge Sort
6. Karatsuba's Multiplication Algorithm

---

## Phase 2 — Divide and Conquer, Partitioning, and Selection

This phase strengthens understanding of recursive decomposition, partitioning, and average-case versus worst-case analysis.

* [ ] Sort-and-Count Inversions
* [ ] Merge-and-Count Split Inversions
* [ ] Naive Partitioning
* [ ] Hoare Partitioning
* [ ] Dutch National Flag Partitioning
* [ ] Quicksort
* [ ] Select Minimum
* [ ] Select Minimum and Maximum
* [ ] Quickselect
* [ ] Median of Medians

Recommended order:

1. Merge-and-Count Split Inversions
2. Sort-and-Count Inversions
3. Select Minimum
4. Select Minimum and Maximum
5. Naive Partitioning
6. Hoare Partitioning
7. Dutch National Flag Partitioning
8. Quicksort
9. Quickselect
10. Median of Medians

---

## Phase 3 — Linear-Time Sorting

These algorithms show that comparison sorting lower bounds can be bypassed when the input has extra structure.

* [ ] Counting Sort
* [ ] Radix Sort

Recommended order:

1. Counting Sort
2. Radix Sort

---

## Phase 4 — Heaps and Priority Queues

Heaps are essential for efficient priority queues and are used in graph algorithms, scheduling, streaming problems, and selection problems.

* [ ] Heap: Rise
* [ ] Heap: Fall
* [ ] Heap: Insert
* [ ] Heap: Delete
* [ ] Heapify
* [ ] Heapsort
* [ ] Fibonacci Heap: Insert
* [ ] Fibonacci Heap: Extract Min
* [ ] Fibonacci Heap: Decrease Key
* [ ] Fibonacci Heap: Delete

Recommended order:

1. Heap: Rise
2. Heap: Fall
3. Heap: Insert
4. Heap: Delete
5. Heapify
6. Heapsort
7. Fibonacci Heap: Insert
8. Fibonacci Heap: Extract Min
9. Fibonacci Heap: Decrease Key
10. Fibonacci Heap: Delete

Note: Fibonacci heaps are advanced. It is reasonable to delay them until after shortest path and minimum spanning tree algorithms.

---

## Phase 5 — Graph Traversal Fundamentals

Graph traversal is the foundation for connectivity, shortest paths, topological sorting, cycle detection, and many interview problems.

* [ ] Generic Depth-First Search
* [ ] Finding Connected Components using DFS
* [ ] Cycle Detection in an Undirected Graph using DFS
* [ ] Generic Breadth-First Search
* [ ] Single-Source Shortest Paths in an Unweighted Graph
* [ ] Reconstruct Shortest Path
* [ ] Connectivity Check

Recommended order:

1. Generic Depth-First Search
2. Finding Connected Components using DFS
3. Cycle Detection in an Undirected Graph using DFS
4. Connectivity Check
5. Generic Breadth-First Search
6. Single-Source Shortest Paths in an Unweighted Graph
7. Reconstruct Shortest Path

---

## Phase 6 — Directed Acyclic Graphs and Topological Ordering

DAG algorithms are important for dependency resolution, scheduling, dynamic programming on graphs, build systems, and compiler-like problems.

* [ ] Topological Sorting using Kahn's Algorithm
* [ ] Topological Sorting using DFS
* [ ] Bottom-Up Longest Path in a DAG
* [ ] Recursive Longest Path in a DAG

Recommended order:

1. Topological Sorting using Kahn's Algorithm
2. Topological Sorting using DFS
3. Bottom-Up Longest Path in a DAG
4. Recursive Longest Path in a DAG

---

## Phase 7 — Union-Find and Minimum Spanning Trees

Union-Find is a small but powerful data structure used in connectivity problems, Kruskal's algorithm, clustering, and graph components.

* [ ] Union-Find using Disjoint-Set Forests without optimizations
* [ ] FIND Operation using Path Compression
* [ ] UNION Operation using Union by Rank
* [ ] Kruskal's Algorithm
* [ ] Prim's Algorithm

Recommended order:

1. Union-Find using Disjoint-Set Forests without optimizations
2. FIND Operation using Path Compression
3. UNION Operation using Union by Rank
4. Kruskal's Algorithm
5. Prim's Algorithm

---

## Phase 8 — Shortest Path Algorithms

Shortest path algorithms are a core graph topic. They also require careful reasoning about edge weights, negative cycles, priority queues, and dynamic programming.

* [ ] Edge Relaxation
* [ ] Dijkstra's Algorithm
* [ ] Improved Dijkstra's Algorithm
* [ ] Bellman-Ford
* [ ] Bellman-Ford: Handling Negative Cycles
* [ ] Floyd-Warshall
* [ ] Warshall's Transitive Closure Algorithm

Recommended order:

1. Edge Relaxation
2. Dijkstra's Algorithm
3. Improved Dijkstra's Algorithm
4. Bellman-Ford
5. Bellman-Ford: Handling Negative Cycles
6. Warshall's Transitive Closure Algorithm
7. Floyd-Warshall

---

## Phase 9 — Dynamic Programming Fundamentals

Dynamic programming is one of the most important topics for interviews and algorithmic problem solving. This phase starts with simple recurrence relations and builds toward table-based reconstruction problems.

* [ ] Recursive Fibonacci Numbers
* [ ] Memoised Fibonacci Numbers
* [ ] Bottom-Up Fibonacci Numbers
* [ ] Top-Down Coin Change
* [ ] Bottom-Up Coin Change
* [ ] Coin Change Solution Reconstruction using Backtracking
* [ ] Bottom-Up Coin Change with Solution Reconstruction using Decision Table
* [ ] Bottom-Up Unbounded Knapsack
* [ ] Bottom-Up 0-1 Knapsack
* [ ] Bottom-Up Edit Distance
* [ ] Optimal Sequence Alignment
* [ ] Optimal Matrix Multiplication

Recommended order:

1. Recursive Fibonacci Numbers
2. Memoised Fibonacci Numbers
3. Bottom-Up Fibonacci Numbers
4. Top-Down Coin Change
5. Bottom-Up Coin Change
6. Coin Change Solution Reconstruction using Backtracking
7. Bottom-Up Coin Change with Solution Reconstruction using Decision Table
8. Bottom-Up Unbounded Knapsack
9. Bottom-Up 0-1 Knapsack
10. Bottom-Up Edit Distance
11. Optimal Sequence Alignment
12. Optimal Matrix Multiplication

---

## Phase 10 — Network Flow and Matching

These algorithms are more advanced, but they are valuable for understanding optimization, constraints, bipartite matching, and graph transformations.

* [ ] Ford-Fulkerson Method
* [ ] Ford-Fulkerson implemented using DFS
* [ ] Method to Solve the Circulation with Demands Problem
* [ ] Hungarian Algorithm

Recommended order:

1. Ford-Fulkerson Method
2. Ford-Fulkerson implemented using DFS
3. Method to Solve the Circulation with Demands Problem
4. Hungarian Algorithm

---

## Phase 11 — Hashing

Hashing is essential for practical software engineering and algorithmic problem solving. Cuckoo hashing is useful for understanding collision resolution strategies beyond chaining and linear probing.

* [ ] Cuckoo Hashing: Lookup
* [ ] Cuckoo Hashing: Deletion
* [ ] Cuckoo Hashing: Insertion

Recommended order:

1. Cuckoo Hashing: Lookup
2. Cuckoo Hashing: Deletion
3. Cuckoo Hashing: Insertion

---

## Phase 12 — Balanced Trees and Search Trees

Tree algorithms are useful for ordered data, indexing, databases, file systems, and understanding how practical data structures maintain balance.

* [ ] AVL Tree: Right Rotation
* [ ] AVL Tree: Left Rotation
* [ ] AVL Tree: Double-Right Rotation
* [ ] AVL Tree: Double-Left Rotation
* [ ] AVL Tree: Rebalance
* [ ] B-Tree: Search
* [ ] B-Tree: Insert
* [ ] B-Tree: Delete

Recommended order:

1. AVL Tree: Right Rotation
2. AVL Tree: Left Rotation
3. AVL Tree: Double-Right Rotation
4. AVL Tree: Double-Left Rotation
5. AVL Tree: Rebalance
6. B-Tree: Search
7. B-Tree: Insert
8. B-Tree: Delete

---

## Phase 13 — Tries, Suffix Structures, and String Indexing

These algorithms are useful for autocomplete, text search, pattern matching, compression, bioinformatics, and compiler-like tooling.

* [ ] Prefix Trie: Insertion
* [ ] Prefix Trie: Lookup
* [ ] Prefix Trie: String Sorting
* [ ] Naive Suffix Array Construction
* [ ] Prefix-Doubling Suffix Array Construction
* [ ] Ukkonen's Algorithm
* [ ] Suffix Array: Pattern Matching

Recommended order:

1. Prefix Trie: Insertion
2. Prefix Trie: Lookup
3. Prefix Trie: String Sorting
4. Naive Suffix Array Construction
5. Prefix-Doubling Suffix Array Construction
6. Suffix Array: Pattern Matching
7. Ukkonen's Algorithm

Note: Ukkonen's algorithm is one of the most advanced algorithms in this repository. It is fine to leave it until late.

---

## Phase 14 — String Matching and Compression

This phase focuses on efficient text processing algorithms.

* [ ] Gusfield Z-Algorithm
* [ ] Pattern Matching using the Z-Algorithm
* [ ] Boyer-Moore Algorithm
* [ ] Knuth-Morris-Pratt Algorithm
* [ ] Burrows-Wheeler Transform
* [ ] Lempel-Ziv LZ77

Recommended order:

1. Gusfield Z-Algorithm
2. Pattern Matching using the Z-Algorithm
3. Knuth-Morris-Pratt Algorithm
4. Boyer-Moore Algorithm
5. Burrows-Wheeler Transform
6. Lempel-Ziv LZ77

---

# Part 2 — Practical Interview and Software Engineering Extensions

These are not all more advanced than the original algorithms. Many are simpler, but they are extremely useful for smaller-company interviews, LeetCode practice, and day-to-day software engineering.

## Phase 15 — Core Data Structures

These are especially important for interviews and practical software engineering. They are intentionally listed after the original university algorithms, but they can be done earlier if interview readiness becomes the priority.

* [ ] Dynamic Array
* [ ] Singly Linked List
* [ ] Doubly Linked List
* [ ] Stack using Array
* [ ] Stack using Linked List
* [ ] Queue using Array
* [ ] Queue using Linked List
* [ ] Circular Queue
* [ ] Deque
* [ ] Hash Table using Separate Chaining
* [ ] Hash Table using Open Addressing
* [ ] Binary Search Tree: Search
* [ ] Binary Search Tree: Insert
* [ ] Binary Search Tree: Delete

---

## Phase 16 — Interview Problem-Solving Patterns

These are not always formal textbook algorithms, but they are some of the most useful patterns for LeetCode-style problem solving.

* [ ] Two Pointers
* [ ] Sliding Window
* [ ] Prefix Sums
* [ ] Difference Array
* [ ] Fast and Slow Pointers
* [ ] Binary Search on Answer
* [ ] Backtracking
* [ ] Subsets Generation
* [ ] Permutations Generation
* [ ] Combinations Generation
* [ ] Matrix Traversal

---

## Phase 17 — Practical Graph Problems and Variants

These are common graph patterns that often appear in interviews in more practical forms than textbook graph algorithms.

* [ ] BFS on a Grid
* [ ] DFS on a Grid
* [ ] Flood Fill
* [ ] Number of Islands
* [ ] Bipartite Graph Check
* [ ] Detect Cycle in a Directed Graph
* [ ] Strongly Connected Components: Kosaraju's Algorithm
* [ ] Strongly Connected Components: Tarjan's Algorithm

---

## Phase 18 — Binary Tree Algorithms

These are more commonly asked in interviews than AVL or B-tree implementation details.

* [ ] Binary Tree Preorder Traversal
* [ ] Binary Tree Inorder Traversal
* [ ] Binary Tree Postorder Traversal
* [ ] Binary Tree Level-Order Traversal
* [ ] Binary Tree Height
* [ ] Binary Tree Diameter
* [ ] Lowest Common Ancestor
* [ ] Validate Binary Search Tree
* [ ] Serialize and Deserialize Binary Tree

---

## Phase 19 — Additional Dynamic Programming Problems

These complement the original university DP algorithms with common interview patterns.

* [ ] Maximum Subarray
* [ ] Climbing Stairs
* [ ] House Robber
* [ ] Longest Common Subsequence
* [ ] Longest Increasing Subsequence
* [ ] Partition Equal Subset Sum
* [ ] Word Break
* [ ] Grid Unique Paths
* [ ] Minimum Path Sum in Grid

---

## Phase 20 — Interval Algorithms

Interval problems are common in practical scheduling, calendar, booking, and resource allocation problems.

* [ ] Merge Intervals
* [ ] Insert Interval
* [ ] Interval Intersection
* [ ] Meeting Rooms
* [ ] Meeting Rooms II

---

## Phase 21 — Additional Greedy Algorithms

These are useful for building intuition around local choices, exchange arguments, and optimization problems.

* [ ] Activity Selection
* [ ] Fractional Knapsack
* [ ] Jump Game
* [ ] Gas Station
* [ ] Huffman Coding

---

## Full Ordered Roadmap

1. Selection Sort
2. Insertion Sort
3. Binary Search
4. Merge
5. Merge Sort
6. Karatsuba's Multiplication Algorithm
7. Merge-and-Count Split Inversions
8. Sort-and-Count Inversions
9. Select Minimum
10. Select Minimum and Maximum
11. Naive Partitioning
12. Hoare Partitioning
13. Dutch National Flag Partitioning
14. Quicksort
15. Quickselect
16. Median of Medians
17. Counting Sort
18. Radix Sort
19. Heap: Rise
20. Heap: Fall
21. Heap: Insert
22. Heap: Delete
23. Heapify
24. Heapsort
25. Generic Depth-First Search
26. Finding Connected Components using DFS
27. Cycle Detection in an Undirected Graph using DFS
28. Connectivity Check
29. Generic Breadth-First Search
30. Single-Source Shortest Paths in an Unweighted Graph
31. Reconstruct Shortest Path
32. Topological Sorting using Kahn's Algorithm
33. Topological Sorting using DFS
34. Bottom-Up Longest Path in a DAG
35. Recursive Longest Path in a DAG
36. Union-Find using Disjoint-Set Forests without optimizations
37. FIND Operation using Path Compression
38. UNION Operation using Union by Rank
39. Kruskal's Algorithm
40. Prim's Algorithm
41. Edge Relaxation
42. Dijkstra's Algorithm
43. Improved Dijkstra's Algorithm
44. Bellman-Ford
45. Bellman-Ford: Handling Negative Cycles
46. Warshall's Transitive Closure Algorithm
47. Floyd-Warshall
48. Recursive Fibonacci Numbers
49. Memoised Fibonacci Numbers
50. Bottom-Up Fibonacci Numbers
51. Top-Down Coin Change
52. Bottom-Up Coin Change
53. Coin Change Solution Reconstruction using Backtracking
54. Bottom-Up Coin Change with Solution Reconstruction using Decision Table
55. Bottom-Up Unbounded Knapsack
56. Bottom-Up 0-1 Knapsack
57. Bottom-Up Edit Distance
58. Optimal Sequence Alignment
59. Optimal Matrix Multiplication
60. Ford-Fulkerson Method
61. Ford-Fulkerson implemented using DFS
62. Method to Solve the Circulation with Demands Problem
63. Hungarian Algorithm
64. Cuckoo Hashing: Lookup
65. Cuckoo Hashing: Deletion
66. Cuckoo Hashing: Insertion
67. AVL Tree: Right Rotation
68. AVL Tree: Left Rotation
69. AVL Tree: Double-Right Rotation
70. AVL Tree: Double-Left Rotation
71. AVL Tree: Rebalance
72. B-Tree: Search
73. B-Tree: Insert
74. B-Tree: Delete
75. Prefix Trie: Insertion
76. Prefix Trie: Lookup
77. Prefix Trie: String Sorting
78. Gusfield Z-Algorithm
79. Pattern Matching using the Z-Algorithm
80. Knuth-Morris-Pratt Algorithm
81. Boyer-Moore Algorithm
82. Naive Suffix Array Construction
83. Prefix-Doubling Suffix Array Construction
84. Suffix Array: Pattern Matching
85. Burrows-Wheeler Transform
86. Lempel-Ziv LZ77
87. Ukkonen's Algorithm
88. Fibonacci Heap: Insert
89. Fibonacci Heap: Extract Min
90. Fibonacci Heap: Decrease Key
91. Fibonacci Heap: Delete
92. Dynamic Array
93. Singly Linked List
94. Doubly Linked List
95. Stack using Array
96. Stack using Linked List
97. Queue using Array
98. Queue using Linked List
99. Circular Queue
100. Deque
101. Hash Table using Separate Chaining
102. Hash Table using Open Addressing
103. Binary Search Tree: Search
104. Binary Search Tree: Insert
105. Binary Search Tree: Delete
106. Two Pointers
107. Sliding Window
108. Prefix Sums
109. Difference Array
110. Fast and Slow Pointers
111. Binary Search on Answer
112. Backtracking
113. Subsets Generation
114. Permutations Generation
115. Combinations Generation
116. Matrix Traversal
117. BFS on a Grid
118. DFS on a Grid
119. Flood Fill
120. Number of Islands
121. Bipartite Graph Check
122. Detect Cycle in a Directed Graph
123. Strongly Connected Components: Kosaraju's Algorithm
124. Strongly Connected Components: Tarjan's Algorithm
125. Binary Tree Preorder Traversal
126. Binary Tree Inorder Traversal
127. Binary Tree Postorder Traversal
128. Binary Tree Level-Order Traversal
129. Binary Tree Height
130. Binary Tree Diameter
131. Lowest Common Ancestor
132. Validate Binary Search Tree
133. Serialize and Deserialize Binary Tree
134. Maximum Subarray
135. Climbing Stairs
136. House Robber
137. Longest Common Subsequence
138. Longest Increasing Subsequence
139. Partition Equal Subset Sum
140. Word Break
141. Grid Unique Paths
142. Minimum Path Sum in Grid
143. Merge Intervals
144. Insert Interval
145. Interval Intersection
146. Meeting Rooms
147. Meeting Rooms II
148. Activity Selection
149. Fractional Knapsack
150. Jump Game
151. Gas Station
152. Huffman Coding

---

## Changelog

Maintain a `CHANGELOG.md` to track meaningful changes over time.

Recommended starting structure:

```md
# Changelog

## Unreleased

### Added

- Initial package structure
- Algorithm roadmap
- ADT contract requirements
- Type annotation and docstring standards
- Visualisation-friendly tracing API plan
```

---

## Benchmarking

Benchmarks live in `benchmarks/` and are designed to compare measured time and
peak Python memory usage with normalized expected complexity curves.

Install benchmark dependencies:

```bash
pip install -e ".[bench]"
```

Run a benchmark suite:

```bash
python -m benchmarks.cli benchmarks.benchmark_sorting
```

The runner writes CSV, JSON, and PNG plots to `benchmark-results/`. Each
`BenchmarkCase` declares:

* an input factory
* the operation being measured
* input sizes
* expected time complexity
* optional expected space complexity

See `docs/benchmarking.md` for the full workflow.

---

## Notes

This repository is a learning project and a reusable package. Some algorithms may have multiple implementations:

* simple educational version
* optimized version
* recursive version
* iterative version
* version with reconstruction or tracing

That is intentional. The purpose is to understand the trade-offs, not just to minimize the number of files.
