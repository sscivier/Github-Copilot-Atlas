# Scientific Python Development Agents

A comprehensive suite of specialized AI agents for scientific Python development, tailored for theoretical and computational geophysics with Gaussian processes, inversions, and forward modeling. These agents follow the [Ten Simple Rules for AI-Assisted Coding in Science](https://arxiv.org/abs/2510.22254) and support modern Python workflows with uv, NumPy, SciPy, PyTorch, GPyTorch, Matplotlib, XArray, and Ruff.

## Overview

The Sci-Agents suite provides orchestrated development workflows with built-in stress-testing and preservation stages for transparency and traceability.

### Agent Roster

1. **Sci-Conductor**: Orchestrator managing the full development lifecycle
2. **Sci-Plan**: Planning with options, tradeoffs, and recommendations
3. **Sci-Research**: Scientific context and best practices research
4. **Sci-Explore**: Fast codebase exploration and pattern discovery
5. **Sci-Implement**: TDD-driven implementation with numerical stability
6. **Sci-Review**: Scientific correctness and quality validation
7. **Sci-Notebook**: Jupyter notebook specialist for exploratory analysis
8. **Sci-Viz**: Visualization using matplotlib

## Development Workflow

### Standard Lifecycle

```text
Planning → Stress-Test → Implementation → Review → Preserve → Commit
```

**Key Stages:**

1. **Planning**: Sci-Plan creates comprehensive plans with implementation options
2. **Stress-Test**: Automatically identify edge cases, failure modes, resource requirements
3. **Implementation**: Sci-Implement follows strict TDD with numerical stability
4. **Review**: Sci-Review validates correctness, reproducibility, quality
5. **Preserve**: Document decisions, assumptions, verifications for traceability
6. **Commit**: User commits with generated message, cycle repeats for next phase

### Stress-Testing

Built-in stress-testing at planning and implementation stages:

- **Edge Cases**: NaN, inf, empty arrays, dimension mismatches, extreme values
- **Numerical Stability**: Matrix conditioning, precision limits, cancellation errors
- **Reproducibility**: Seed management, determinism, device compatibility
- **Resource Requirements**: Memory usage, computational complexity, GPU needs
- **Test Coverage**: Unit, integration, property-based, GPU-ready tests

### Preservation & Traceability

After each phase, preservation documents capture:

- **Decisions Made**: What approaches were chosen and why
- **Assumptions**: What was assumed and how validated
- **Verifications**: What was tested and how
- **Trade-offs**: What was sacrificed and why

Format: `plans/<task>/phase-<N>-preserve.md`

## Agent Details

### Sci-Conductor (Orchestrator)

**Model**: Claude Sonnet 4.5

**Role**: Manages the full development lifecycle, coordinates all subagents

**When to Use**: Start here for any multi-phase scientific development task

**Key Features**:

- Context-aware delegation to specialized subagents
- Built-in stress-testing coordination
- Preservation stage after each phase
- User approval gates at critical points

**Invocation**:

```text
@Sci-Conductor

I need to implement a new Gaussian process kernel with spatially-varying lengthscales using a neural network. The kernel should work with GPyTorch and be numerically stable.
```

### Sci-Plan (Planning Agent)

**Model**: Claude Opus 4.6

**Role**: Creates comprehensive implementation plans with options and tradeoffs

**Key Features**:

- Presents 2-3 options for major design decisions
- Includes stress-test considerations
- Specifies test strategy (unit, integration, property-based)
- Addresses reproducibility requirements
- Markdownlint-compliant plans

**Typical Output**:

- Multi-phase plan (3-10 phases)
- Implementation options with pros/cons
- Stress-test considerations
- Reproducibility checklist
- Scientific validation checklist

### Sci-Research (Research Agent)

**Model**: GPT-5.2

**Role**: Gathers scientific context, algorithm details, best practices

**Key Features**:

- Researches numerical methods and algorithms
- Consults official documentation (NumPy, PyTorch, GPyTorch, uv, etc.)
- Identifies edge cases and failure modes
- Provides implementation options with tradeoffs
- Delegates to Sci-Explore for codebase discovery

**Example Tasks**:

- Research GP hyperparameter optimization strategies
- Find best practices for testing stochastic models
- Investigate numerical stability patterns for PDEs
- Compare inducing point initialization methods

### Sci-Explore (Exploration Agent)

**Model**: Claude Haiku 4.5

**Role**: Fast codebase exploration and pattern discovery

**Key Features**:

- Parallel search strategy (semantic, grep, file search)
- Understands scientific Python project structures
- Recognizes test organization (unit, integration, properties, GPU-ready)
- Maps dependencies quickly
- Read-only operation (safe exploration)

**Output Format**:

```xml
<results>
<files>
- /path/to/file.py: Brief relevance note
</files>
<answer>
Explanation of what was found
</answer>
<next_steps>
- Actionable step 1
- Actionable step 2
</next_steps>
</results>
```

### Sci-Implement (Implementation Agent)

**Model**: Claude Sonnet 4.5

**Role**: Implements scientific Python code with strict TDD

**Key Features**:

- Strict TDD workflow (red → green → refactor)
- Numerical stability expertise (log-space, Cholesky, conditioning)
- Edge case testing (NaN, inf, empty, dimension mismatches)
- Device-agnostic code (CPU/GPU compatible)
- Type hints and Google-style docstrings
- uv workflow integration

**Quality Checks**:

- `uv run pytest` (all tests pass)
- `uv run ruff check --fix .` (linting)
- `uv run ruff format .` (formatting)
- `uv run mypy .` (type checking)

### Sci-Review (Review Agent)

**Model**: Claude Opus 4.6

**Role**: Validates scientific correctness and code quality

**Review Criteria**:

- **Scientific Correctness**: Algorithm implementation, mathematical soundness
- **Numerical Stability**: Stable computation, appropriate precision
- **Reproducibility**: Seed management, determinism, device compatibility
- **Test Coverage**: Unit, integration, property, edge cases, GPU-ready
- **Code Quality**: Type hints, documentation, style
- **Performance**: Complexity, vectorization, memory efficiency

**Output**: Structured review with APPROVED / NEEDS_REVISION / FAILED status

### Sci-Notebook (Notebook Agent)

**Model**: Claude Sonnet 4.5

**Role**: Creates Jupyter notebooks for exploration and documentation

**Use Cases**:

- Exploratory data analysis (EDA)
- Method demonstrations
- Tutorials with runnable examples
- Reproducible research documentation

**Best Practices**:

- Narrative-driven structure (markdown + code)
- Reproducibility (seeds, environment docs)
- Clear visualizations
- Run-all verification
- Extract production code to modules

**Invocation**:

```text
@Sci-Notebook

Create a tutorial notebook demonstrating how to use our custom Gibbs kernel with GPyTorch, including visualization of the spatially-varying lengthscales.
```

### Sci-Viz (Visualization Agent)

**Model**: Claude Sonnet 4.5, Gemini 3 Pro

**Role**: Creates scientific visualizations

**Capabilities**:

- **Spatial Data**: 2D heatmaps, contour plots, map projections
- **Uncertainty**: Confidence bands, prediction intervals
- **Time Series**: Temporal evolution with proper date formatting
- **3D Surfaces**: Surface plots, volume rendering
- **Comparisons**: Multi-panel figures, subplots

**Standards**:

- Colorblind-friendly colormaps (e.g., viridis, plasma, cividis)
- Complete labels with units
- Vector formats (PDF, SVG) + high-res raster (300 DPI PNG)
- Accessibility features
- Edge case handling (NaN, inf, outliers)

## Ten Simple Rules Integration

| Rule | Agent(s) | Implementation |
| ------ | ---------- | --------------- |
| 1. Gather Domain Knowledge | Sci-Research, Sci-Plan | Research phase before planning |
| 2. Problem Framing | Sci-Plan | Distinguish scientific problem from code |
| 3. Interaction Model | Sci-Conductor | Orchestration with specialized subagents |
| 4. Solution Thinking | Sci-Plan | Options, tradeoffs, recommendations |
| 5. Context Management | All | Structured handoffs, preservation docs |
| 6. Test-Driven Development | Sci-Implement | Strict TDD: tests first, minimal code |
| 7. Test Planning | Sci-Plan, Sci-Implement | Comprehensive test strategy |
| 8. Monitor Progress | Sci-Conductor | Phase tracking, stress-testing |
| 9. Critical Review | Sci-Review | Scientific correctness validation |
| 10. Incremental Refinement | Sci-Conductor | Phase-by-phase development cycle |

## Usage Examples

### Example 1: Implement New GP Kernel

```text
@Sci-Conductor

I need to implement a new kernel for Gaussian processes that handles discontinuities 
in geophysical fields (e.g., across fault boundaries). The kernel should:
- Inherit from gpytorch.kernels.Kernel
- Take a discontinuity mask as input
- Handle both stationary and non-stationary lengthscales
- Be numerically stable and GPU-compatible
- Include comprehensive tests
```

**Workflow**:

1. Sci-Plan creates plan with options (indicator covariance, windowed kernels, etc.)
2. Stress-test identifies edge cases (discontinuity boundaries, numerical stability)
3. Sci-Implement creates tests first, then implements kernel
4. Sci-Review validates correctness and GPU compatibility
5. Preservation documents design decisions and trade-offs
6. User commits, cycle continues for next phase

### Example 2: Exploratory Data Analysis

```text
@Sci-Notebook

Create an EDA notebook for our new gravity anomaly dataset. I need to:
- Load the XArray dataset
- Visualize spatial coverage and data quality
- Explore correlations with existing geological data
- Identify preprocessing needs (outliers, missing data)
- Visualize spatial correlation structure
```

**Workflow**:

1. Sci-Notebook creates structured notebook with narrative
2. Loads data with inspection and validation
3. Creates visualizations (delegates complex plots to Sci-Viz if needed)
4. Documents findings and recommendations
5. Extracts any reusable preprocessing code to modules

### Example 3: Publication Figure

```text
@Sci-Viz

Create a publication-quality figure showing:
- 3x2 panel grid
- Top row: GP predictions (mean, variance, observations)
- Bottom row: Residuals, Q-Q plot, spatial correlation of residuals
- Colorblind-friendly, vector format (PDF + PNG)
- Include all labels with units, shared colorbars
```

**Workflow**:

1. Sci-Viz creates multi-panel figure with matplotlib
2. Applies publication standards (fonts, colormaps, resolution)
3. Handles edge cases (missing data, outliers)
4. Saves in multiple formats
5. Provides code for reproducibility

## Configuration

### Plan Directory

By default, plans and preservation documents are stored in `plans/` with subdirectories for each task (e.g., `plans/<task-name>/`).

To customize, create `AGENTS.md` in workspace root:

```markdown
# Agent Configuration

## Plan Directory

All plan and preservation documents should be stored in `.sci/plans/` with subdirectories per task.
```

Agents will automatically use the configured directory and create task subdirectories.

### Environment Setup

These agents expect projects using:

- **Python**: 3.12+ (managed with uv)
- **Package Manager**: uv (<https://docs.astral.sh/uv/>)
- **Key Libraries**: NumPy, SciPy, PyTorch, GPyTorch, XArray, Matplotlib
- **Code Quality**: Ruff (linting + formatting), mypy (type checking)
- **Testing**: pytest, hypothesis, pytest-cov

**Example `pyproject.toml` structure**:

```toml
[project]
name = "your-project"
requires-python = ">=3.12"
dependencies = [
    "numpy>=2.0",
    "scipy>=1.14",
    "torch>=2.5",
    "gpytorch>=1.12",
    "matplotlib>=3.9",
    "xarray>=2024.0",
]

[project.optional-dependencies]
cpu = ["torch>=2.5"]
cuda = ["torch>=2.5"]

[tool.uv]
conflicts = [[{ extra = "cpu" }, { extra = "cuda" }]]

[dependency-groups]
dev = ["ruff>=0.8", "mypy>=1.13"]
test = ["pytest>=8.0", "pytest-cov>=6.0", "hypothesis>=6.0"]

[tool.pytest.ini_options]
testpaths = ["tests"]
markers = [
    "unit: fast unit tests",
    "integration: multi-component tests",
    "properties: hypothesis property tests",
    "gpu_ready: device compatibility tests",
]

[tool.ruff.lint]
select = ["E", "F", "UP", "B", "SIM", "I", "D"]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

## Best Practices

### For Developers

1. **Start with Sci-Conductor**: Orchestration handles complexity
2. **Review stress-test findings**: Address concerns early
3. **Preserve decisions**: Transparency prevents future confusion
4. **Commit after each phase**: Incremental progress, easy rollback
5. **Extract notebook code**: Move tested code to modules

### For Scientific Code

1. **Test numerical stability**: Check conditioning, use stable algorithms
2. **Design device-agnostic**: Works on CPU and GPU without changes
3. **Ensure reproducibility**: Seeds in tests, deterministic algorithms
4. **Validate scientifically**: Known solutions, conservation laws, invariants
5. **Document thoroughly**: Google-style docstrings with equations and units

### For Reproducibility

1. **Set seeds in fixtures**: Not in implementation code
2. **Use deterministic algorithms**: Specify in test fixtures
3. **Test on multiple dtypes**: float32 and float64
4. **Create GPU-ready tests**: Device compatibility without actual GPU
5. **Version critical dependencies**: Pin when necessary

## Limitations

- Agents are optimized for scientific Python, may be less effective for other domains
- Stress-testing is automated but may miss domain-specific edge cases
- Preservation documents require manual review for completeness
- GPU testing is limited to compatibility checks (actual GPU testing requires hardware)

## Contributing

To extend or modify agents:

1. Agent definitions are in `sci-agents/*.agent.md`
2. Follow existing agent structure (YAML frontmatter + Markdown)
3. Maintain consistency with Ten Simple Rules principles
4. Test with representative scientific computing tasks
5. Ensure `markdownlint` compliance

## License

See repository license.

## Citation

If using these agents in research, please cite:

- This repository: [Github-Copilot-Atlas](https://github.com/sscivier/Github-Copilot-Atlas)
- Ten Simple Rules paper: [Ten Simple Rules for AI-Assisted Coding in Science](https://arxiv.org/abs/2510.22254)

## Acknowledgments

Based on the [Github-Copilot-Atlas](https://github.com/bigguy345/Github-Copilot-Atlas) framework and inspired by [copilot-orchestra](https://github.com/ShepAlderson/copilot-orchestra).

Follows principles from "Ten Simple Rules for AI-Assisted Coding in Science" by Bridgeford et al.
