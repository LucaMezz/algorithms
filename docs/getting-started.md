# Getting Started

## Prerequisites

- Python 3.11 or later
- Node.js with `npm` (for Husky commit hooks and commitlint)

## Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/LucaMezz/algorithms.git
cd algorithms
```

Run `make install` to create a virtual environment, install all development
dependencies, and install the Node.js tooling for Husky:

```bash
make install
```

This is equivalent to:

```bash
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -e ".[dev]"
npm install
```

## Git Hooks

Two hooks fire automatically on every commit:

- **pre-commit** (Husky → `.venv/bin/pre-commit run`): runs ruff and mypy on
  staged files via `.pre-commit-config.yaml`.
- **commit-msg** (Husky → commitlint): validates the commit message format
  against conventional commits.

The hooks are wired through Husky, which is set up by `npm install`. No extra
step is needed after `make install`.

To keep the pre-commit hook tool versions up to date, run:

```bash
.venv/bin/pre-commit autoupdate
```

## Running Quality Checks

Run all checks at once:

```bash
make check
```

Or run them individually:

```bash
make format     # ruff format .
make lint       # ruff check .
make typecheck  # mypy src
make test       # pytest
```

Equivalent commands using the venv directly:

```bash
.venv/bin/ruff format .
.venv/bin/ruff check .
.venv/bin/mypy src
.venv/bin/pytest
```

## Benchmarks

Install benchmark dependencies (matplotlib for plots):

```bash
make install-bench
```

Run a benchmark suite:

```bash
.venv/bin/python -m benchmarks.cli benchmarks.benchmark_sorting
```

See `docs/benchmarking.md` for a full walkthrough.

## Documentation

Install documentation dependencies:

```bash
make install-docs
```

Serve the docs site locally with live reload:

```bash
make docs-serve
```

Build the static site to `site/`:

```bash
make docs
```

### Docstring Format

All public functions, methods, and classes use **Google-style docstrings**.
The `mkdocstrings` plugin parses these to generate the API reference.

Function template:

```python
def example(values: Sequence[int], target: int) -> int | None:
    """One-line summary in imperative mood, ending with a period.

    Optional extended description for non-obvious behavior.

    Args:
        values: Description of the first parameter.
        target: Description of the second parameter.

    Returns:
        Description of the return value.

    Raises:
        ValueError: When and why this is raised. Omit if no exceptions.

    Time complexity:
        O(log n).

    Space complexity:
        O(1).
    """
```

Class template:

```python
class ArrayStack(Stack[T]):
    """One-line summary of what the class is.

    Longer description if the class has non-obvious behavior or invariants.
    For data structures, include the ADT it satisfies and a brief
    complexity summary for the key operations.
    """
```

Rules:
- The first line is a short summary in imperative mood ("Return...", "Sort...", "Insert...").
- `Args`, `Returns`, and `Raises` only appear when they add information not
  already obvious from the type annotations.
- `Time complexity` and `Space complexity` are required for all algorithm and
  data structure implementations.
- Private helpers do not require docstrings unless the logic is non-obvious.

## Editor Setup

The project's type checker is **mypy**, run via `make typecheck` and in CI.

For in-editor diagnostics, any pyright-based editor (Neovim with pyright LSP,
VS Code with Pylance) needs to know where the virtual environment is. Create a
local `pyrightconfig.json` in the project root — it is gitignored and does not
affect the project's toolchain:

```json
{
  "venvPath": ".",
  "venv": ".venv"
}
```

In Neovim specifically:

- **Pyright** handles type checking diagnostics and hover documentation.
- **Ruff LSP** handles linting diagnostics (unused imports, style issues, etc.).
- **conform.nvim** runs `ruff format` on save.

If Neovim shows import errors after a fresh clone, ensure the virtual
environment exists (`make install`) and restart the LSP with `:LspRestart`.
