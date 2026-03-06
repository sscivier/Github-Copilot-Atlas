---
name: sci-init
description: Generate or update AGENTS.md for a scientific Python project
agent: Sci-Conductor
argument-hint: Optionally specify a focus area (e.g. GP models, XArray pipelines, visualization)
---

Related agent: `Sci-Conductor`. Related skill: `agent-customization`.

Generate or update the workspace instructions file (`AGENTS.md` as first choice, or `.github/copilot-instructions.md` if already present) to guide AI coding agents in this scientific Python project.

## Discovery

Search for existing AI conventions and project metadata using this glob pattern:
`**/{AGENTS.md,.github/copilot-instructions.md,AGENT.md,CLAUDE.md,.cursorrules,pyproject.toml,uv.lock,setup.py,README.md,.pre-commit-config.yaml}`

Then research the project to discover:

- **Python toolchain**: `uv`, `pip`, or `conda`; check for `uv.lock`, `requirements.txt`, `environment.yml`
- **Test framework**: `pytest` configuration, markers (`gpu_ready`, `slow`, `integration`), fixture conventions, snapshot directories
- **Linting / formatting**: `ruff`, `ty`, `pre-commit` hooks and their commands
- **Scientific domain**: GPs, PDEs, geophysics, climate, neuroscience, etc.
- **Core libraries**: PyTorch, GPyTorch, XArray, NumPy, SciPy, Matplotlib, Cartopy, Hypothesis, etc.
- **Data layout**: directory paths, file formats (NetCDF, HDF5, CSV, Zarr), XArray Dataset schema conventions
- **Model architecture**: kernel naming, objective functions, training loops, prediction conventions
- **Reproducibility**: random seed management, deterministic algorithm flags, experiment tracking tools

## Output Format

Generate concise, actionable instructions (~30–60 lines) using this structure. Only include sections that are applicable to THIS project.

```markdown
# {Project Name} — Agent Guidelines

## Environment
- Install: `uv sync` (or equivalent)
- Python version: {version}
- Run tests: `uv run pytest`

## Code Style
- Format: `uv run ruff format .`
- Lint: `uv run ruff check --fix .`
- Type check: `uv run ty check src/`
- Docstrings: Google-style

## Architecture
- {Core module layout and purpose of each top-level package}
- {Scientific domain conventions: kernel naming, model structure, etc.}
- {Data formats: XArray Dataset schemas, expected tensor shapes, dtype conventions}

## Testing
- Runner: `uv run pytest`
- Structure: `tests/unit/`, `tests/integration/`, `tests/properties/`
- Markers: `@pytest.mark.gpu_ready`, `@pytest.mark.slow`
- Property tests: Hypothesis for mathematical invariants

## Reproducibility
- Seeds: set only in test fixtures, never in production code
- Determinism: `torch.use_deterministic_algorithms(True)` in tests
- {Data versioning approach if present}

## Scientific Conventions
- {Domain-specific patterns and idioms discovered in this project}
- {Numerical stability conventions: log-space, Cholesky, etc.}
```

## Guidelines

- If an instructions file already exists, merge intelligently without removing existing content
- Write concise, actionable instructions — avoid generic advice, focus on THIS project's specific approaches
- List build/test/lint commands explicitly — agents will run them automatically
- After updating the file, ask for feedback on any unclear or incomplete sections
