# Contributing

Thanks for your interest in contributing. This project is both a portfolio piece
and a reusable package, so contributions should make the implementations clearer,
more correct, better tested, or easier to learn from.

## Development Setup

```bash
python -m pip install -e ".[dev]"
```

## Before Opening a Pull Request

Run the local quality checks:

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy src
python -m pytest
```

If you intentionally skip a check, mention why in the pull request.

## Implementation Guidelines

- Implement algorithm and data structure behavior from scratch.
- Keep public functions and classes typed.
- Prefer clear names and direct control flow over clever compact code.
- Document time and space complexity for public implementations.
- Include tests for normal cases, edge cases, and invalid input.
- Keep abstract data type definitions separate from concrete implementations.
- Avoid adding third-party runtime dependencies unless they are clearly needed.

## Adding an Algorithm or Data Structure

1. Place the implementation in the most specific existing package under
   `src/algorithms/`.
2. Add or update tests under `tests/`.
3. Add a short example when usage is not obvious.
4. Update documentation or complexity notes when the public API changes.
5. Add benchmark coverage when performance tradeoffs are central to the change.

## Style

The project uses Ruff for linting and formatting, MyPy for type checking, and
Pytest for tests. Let those tools settle style questions wherever possible.

## Pull Request Checklist

- The change is focused and explained clearly.
- Tests cover the behavior being added or changed.
- Public APIs include type hints and complexity notes.
- Documentation, examples, or benchmarks are updated where useful.
- The changelog is updated for user-visible changes.

## Reporting Issues

For bugs, include the expected behavior, actual behavior, a minimal reproduction,
and the Python version. For algorithm requests, include the name of the
algorithm, the problem it solves, and any reference material that would help
review correctness.
