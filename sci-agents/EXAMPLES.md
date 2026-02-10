# Scientific Python Agents - Usage Examples

This document provides concrete examples of using the Sci-Agents suite for common scientific computing tasks.

## Table of Contents

- [Example 1: Implement Custom GP Kernel](#example-1-implement-custom-gp-kernel)
- [Example 2: Create Data Processing Pipeline](#example-2-create-data-processing-pipeline)
- [Example 3: Exploratory Notebook](#example-3-exploratory-notebook)
- [Example 4: Publication Figure](#example-4-publication-figure)
- [Example 5: Optimization Algorithm](#example-5-optimization-algorithm)

## Example 1: Implement Custom GP Kernel

### Scenario

You need to implement a Gibbs kernel (non-stationary) with neural network-based lengthscale function for modeling geophysical fields with varying smoothness.

### User Request: Gibbs Kernel Implementation

```text
@Sci-Conductor

I need to implement a Gibbs (non-stationary RBF) kernel for GPyTorch where the 
lengthscale varies spatially based on a neural network. Requirements:

- Inherit from gpytorch.kernels.Kernel
- Neural network takes coordinates as input, outputs lengthscale
- Kernel should compute k(x, x') = exp(-0.5 * ||x - x'||^2 / l(x)l(x'))
- Support both 2D and 3D coordinates
- GPU compatible and numerically stable
- Include comprehensive tests (unit, property-based, GPU-ready)

The neural network should be simple (2-3 hidden layers, ReLU activations).
```

### Expected Workflow: Gibbs Kernel

#### Phase 1: Planning

Sci-Plan creates plan with:

- **Options for lengthscale network architecture**:
  - Option A: Single shared MLP
  - Option B: Separate networks for each dimension
  - Recommendation: Option A (simpler, sufficient for most cases)

- **Stress-test considerations**:
  - Near-zero lengthscales (numerical instability)
  - Very different lengthscales at x and x' (asymmetry)
  - Extreme coordinate values
  - GPU memory for large kernel matrices

- **3 Implementation Phases**:
  1. Lengthscale neural network with constraints
  2. Gibbs kernel computation with stability
  3. GPyTorch integration and hyperparameter optimization

#### Phase 2-4: Implementation Cycles

For each phase:

1. **Implement** (Sci-Implement):
   - Write tests first (TDD)
   - Implement with numerical stability
   - Verify tests pass

2. **Review** (Sci-Review):
   - Validate correctness
   - Check stability measures
   - Verify test coverage

3. **Preserve**:
   - Document design decisions (activation functions, initialization)
   - Record assumptions (lengthscale bounds, network capacity)
   - Capture verifications (PSD tests, gradient checks)

4. **Commit**:
   - User commits with generated message
   - Proceed to next phase

### Key Code Artifacts

**Test file** (`tests/unit/test_gibbs_kernel.py`):

```python
@pytest.mark.unit
def test_gibbs_kernel_basic(device, dtype):
    """Test basic Gibbs kernel computation."""
    lengthscale_net = LengthscaleNN(input_dim=2, hidden_dims=[32, 32])
    kernel = GibbsKernel(lengthscale_net)
    
    x1 = torch.randn(10, 2, device=device, dtype=dtype)
    x2 = torch.randn(5, 2, device=device, dtype=dtype)
    
    K = kernel(x1, x2).to_dense()
    
    assert K.shape == (10, 5)
    assert torch.all(K > 0)
    assert torch.all(K <= 1.0 + 1e-6)

@pytest.mark.properties
@given(n1=st.integers(1, 20), n2=st.integers(1, 20))
def test_gibbs_kernel_properties(n1, n2):
    """Test mathematical properties of Gibbs kernel."""
    kernel = GibbsKernel(LengthscaleNN(input_dim=2))
    x1 = torch.randn(n1, 2)
    x2 = torch.randn(n2, 2)
    
    K = kernel(x1, x2).to_dense()
    
    # Bounded
    assert torch.all(K <= 1.0 + 1e-6)
    assert torch.all(K > 0)
    
    # PSD if x1 == x2
    if n1 == n2 and torch.allclose(x1, x2):
        eigvals = torch.linalg.eigvalsh(K)
        assert torch.all(eigvals >= -1e-6)
```

**Implementation** (`src/package/kernels/gibbs.py`):

```python
class LengthscaleNN(nn.Module):
    """Neural network for spatially-varying lengthscales."""
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Compute positive lengthscales.
        
        Uses softplus activation on output to ensure positivity
        and adds small epsilon for numerical stability.
        """
        h = self.network(x)
        return F.softplus(h) + 1e-6  # Positive + stable

class GibbsKernel(gpytorch.kernels.Kernel):
    """Gibbs (non-stationary RBF) kernel with NN lengthscales."""
    
    def forward(self, x1, x2, **params):
        """Compute Gibbs kernel matrix."""
        # Get lengthscales
        l1 = self.lengthscale_net(x1).unsqueeze(-1)  # (n1, 1)
        l2 = self.lengthscale_net(x2).unsqueeze(-2)  # (1, n2)
        
        # Geometric mean for stability
        l_mean = torch.sqrt(l1 * l2)
        
        # Squared distances
        sq_dist = self.covar_dist(x1, x2, square_dist=True)
        
        # Gibbs kernel (log-space for stability)
        log_K = -0.5 * sq_dist / (l_mean ** 2)
        return log_K.exp()
```

## Example 2: Create Data Processing Pipeline

### Scenario: Gravity Anomaly Data Processing

You have gravity anomaly data that needs preprocessing before GP modeling: loading from NetCDF, handling missing data, spatial interpolation, and normalization.

### User Request: Gravity Anomaly Processing Pipeline

```text
@Sci-Conductor

I need a data processing pipeline for gravity anomaly data stored in NetCDF format.
The pipeline should:

1. Load XArray dataset with spatial coordinates (lon, lat, elevation)
2. Handle missing data (interpolate or mask)
3. Remove outliers (beyond 3 sigma)
4. Spatially interpolate to regular grid if needed
5. Normalize data (zero mean, unit variance) with reversible transform
6. Save preprocessed data and normalization parameters

The pipeline should be device-agnostic (CPU/GPU) and preserve all metadata.
```

### Expected Workflow: Data Pipeline

**Planning Phase**:

- Options for interpolation (nearest, linear, kriging)
- Options for outlier handling (remove, cap, or flag)
- Options for missing data (interpolate, mask, or impute)

**Implementation Phases**:

1. Data loading and validation
2. Outlier detection and handling
3. Spatial interpolation
4. Normalization with parameter saving
5. Integration tests with real data

**Stress-Testing**:

- Empty regions (no data)
- Extreme outliers
- Memory usage for large datasets
- Coordinate reference system handling

## Example 3: Exploratory Notebook

### Scenario: Seismic Velocity Dataset Exploration

You received a new seismic velocity dataset and need to explore it before modeling.

### User Request: Seismic Velocity EDA Notebook

```text
@Sci-Notebook

Create an EDA notebook for our new 3D seismic velocity dataset (velocity_field.nc).
I need to:

1. Load and inspect the XArray dataset structure
2. Visualize spatial coverage (2D slices at different depths)
3. Examine statistical distributions (histograms, Q-Q plots)
4. Explore spatial correlation structure (variograms)
5. Identify data quality issues (gaps, outliers, artifacts)
6. Visualize depth profiles at key locations
7. Document findings and recommend preprocessing steps

Include reproducibility setup and clear narrative explanations.
```

### Expected Output: Notebook Structure

Notebook structure:

```markdown
# Seismic Velocity Dataset - Exploratory Analysis

## Overview
Analysis of 3D seismic velocity field for [region]. Dataset spans ...

## Setup
```

```python
# Imports and configuration
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

SEED = 42
np.random.seed(SEED)

# Dataset info
data = xr.open_dataset('velocity_field.nc')
print(data)
```

```markdown
## 1. Data Structure

### Dimensions
- Spatial: 200 x 150 x 50 (lon x lat x depth)
- Coverage: [coordinates]
- Resolution: [spacing]

### Variables
- `velocity`: P-wave velocity (km/s)
- `uncertainty`: Measurement uncertainty
```

```python
# Basic statistics
data['velocity'].describe()
```

```markdown
## 2. Spatial Coverage

Visualizing velocity at different depths:
```

```python
# Create multi-depth visualization
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
depths = [0, 5, 10, 20, 30, 40]

for ax, depth in zip(axes.flat, depths):
    data['velocity'].sel(depth=depth, method='nearest').plot(
        ax=ax, cmap='viridis', vmin=3, vmax=8
    )
    ax.set_title(f'Depth = {depth} km')
    
plt.tight_layout()
plt.show()
```

```markdown
**Observations:**
- Surface shows high variability (sedimentary layers)
- Velocity increases with depth (expected)
- Linear feature at depth=20km (possible fault?)
- Missing data in NE corner (investigate)
```

And so on...

## Example 4: Publication Figure

### Scenario: Multi-Kernel GP Comparison Figure

You need a publication-quality figure comparing GP predictions with different kernels.

### User Request: GP Kernel Comparison Figure

```text
@Sci-Viz

Create a publication figure comparing three GP models (RBF, Matérn, Gibbs kernels)
on our test dataset. Figure should have:

Layout:
- 3x2 grid (3 rows for kernels, 2 columns for mean/variance predictions)
- Shared colorbars within columns
- Training data points overlaid as red dots

Requirements:
- Colorblind-friendly colormaps (viridis for mean, plasma for variance)
- All labels with units (Temperature in °C)
- Vector format (PDF) + high-res PNG (300 DPI)
- Figure size: 12" x 15"
- Annotations showing RMSE on each subplot
- Overall title: "GP Kernel Comparison"

Data files: predictions_rbf.npz, predictions_matern.npz, predictions_gibbs.npz
Training data: training_data.csv
```

### Expected Output: Publication Figure Script

Python script with publication-quality figure:

```python
import matplotlib.pyplot as plt
import numpy as np

# Load data
rbf = np.load('predictions_rbf.npz')
matern = np.load('predictions_matern.npz')
gibbs = np.load('predictions_gibbs.npz')
train = np.loadtxt('training_data.csv', delimiter=',', skiprows=1)

# Publication style
plt.rcParams['figure.figsize'] = (12, 15)
plt.rcParams['font.size'] = 11
plt.rcParams['savefig.dpi'] = 300

fig, axes = plt.subplots(3, 2, figsize=(12, 15))

data_list = [
    (rbf, 'RBF Kernel'),
    (matern, 'Matérn Kernel'),
    (gibbs, 'Gibbs Kernel'),
]

for row, (data, label) in enumerate(data_list):
    # Mean predictions
    ax_mean = axes[row, 0]
    im_mean = ax_mean.pcolormesh(
        data['x'], data['y'], data['mean'],
        cmap='viridis', vmin=-2, vmax=2, shading='auto'
    )
    ax_mean.scatter(train[:, 0], train[:, 1], c='red', 
                   s=20, edgecolor='black', linewidth=0.5)
    ax_mean.set_title(f'{label} - Mean')
    ax_mean.set_ylabel('Latitude (°N)')
    ax_mean.text(0.05, 0.95, f"RMSE: {data['rmse']:.3f}",
                transform=ax_mean.transAxes, 
                verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Variance predictions
    ax_var = axes[row, 1]
    im_var = ax_var.pcolormesh(
        data['x'], data['y'], data['variance'],
        cmap='plasma', vmin=0, vmax=1, shading='auto'
    )
    ax_var.set_title(f'{label} - Variance')
    
    # X labels only on bottom row
    if row == 2:
        ax_mean.set_xlabel('Longitude (°E)')
        ax_var.set_xlabel('Longitude (°E)')

# Shared colorbars
fig.colorbar(im_mean, ax=axes[:, 0], label='Temperature (°C)', 
            fraction=0.046, pad=0.04)
fig.colorbar(im_var, ax=axes[:, 1], label='Variance (°C²)',
            fraction=0.046, pad=0.04)

fig.suptitle('GP Kernel Comparison', fontsize=16, y=0.995)

# Save
plt.savefig('gp_kernel_comparison.pdf', bbox_inches='tight')
plt.savefig('gp_kernel_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Figures saved: gp_kernel_comparison.{pdf,png}")
```

## Example 5: Optimization Algorithm

### Scenario: Custom GP Hyperparameter Optimizer

Implement a custom optimizer for GP hyperparameters with learning rate scheduling and early stopping.

### User Request: GP Hyperparameter Optimization with Early Stopping

```text
@Sci-Conductor

I need a custom training function for GP hyperparameter optimization that includes:

1. Adam optimizer with learning rate scheduling (reduce on plateau)
2. Early stopping based on validation loss
3. Gradient clipping for stability
4. Loss logging and visualization
5. Model checkpointing (save best model)
6. Support for both CPU and GPU

The function should work with GPyTorch models and handle the 
MarginalLogLikelihood objective. Include comprehensive tests.
```

### Expected Workflow: Optimizer

**Planning**:

- **Options for LR scheduling**: ReduceLROnPlateau vs CosineAnnealing vs Exponential
- **Options for early stopping**: Validation loss vs training loss patience
- **Options for checkpointing**: Save every N epochs vs best only

**Stress-Test Considerations**:

- Non-convergence (oscillating loss)
- Numerical instability during optimization
- Memory issues with large models
- Device compatibility

**Implementation Phases**:

1. Basic training loop with Adam
2. Add LR scheduling and early stopping
3. Add checkpointing and logging
4. Integration with GPyTorch models
5. Comprehensive tests

**Key Implementation** (`src/package/training/optimize.py`):

```python
def train_gp(
    model: gpytorch.models.GP,
    likelihood: gpytorch.likelihoods.Likelihood,
    train_x: torch.Tensor,
    train_y: torch.Tensor,
    val_x: Optional[torch.Tensor] = None,
    val_y: Optional[torch.Tensor] = None,
    num_epochs: int = 1000,
    lr: float = 0.1,
    patience: int = 50,
    checkpoint_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Train GP model with early stopping and checkpointing.
    
    Args:
        model: GPyTorch model
        likelihood: GPyTorch likelihood
        train_x: Training inputs
        train_y: Training targets
        val_x: Optional validation inputs
        val_y: Optional validation targets
        num_epochs: Maximum training epochs
        lr: Initial learning rate
        patience: Early stopping patience
        checkpoint_path: Path to save best model
        
    Returns:
        Dictionary with training history and best model state
    """
    # Setup
    model.train()
    likelihood.train()
    
    optimizer = torch.optim.Adam([
        {'params': model.parameters()},
        {'params': likelihood.parameters()},
    ], lr=lr)
    
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='min', factor=0.5, patience=10
    )
    
    mll = gpytorch.mlls.ExactMarginalLogLikelihood(likelihood, model)
    
    # Training loop with checks
    history = {'train_loss': [], 'val_loss': []}
    best_loss = float('inf')
    patience_counter = 0
    
    for epoch in range(num_epochs):
        optimizer.zero_grad()
        
        # Forward pass
        output = model(train_x)
        loss = -mll(output, train_y)
        
        # Backward pass with gradient clipping
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        
        # Validation
        if val_x is not None:
            model.eval()
            with torch.no_grad():
                val_output = model(val_x)
                val_loss = -mll(val_output, val_y)
            model.train()
            
            history['val_loss'].append(val_loss.item())
            scheduler.step(val_loss)
            
            # Early stopping check
            if val_loss < best_loss:
                best_loss = val_loss
                patience_counter = 0
                if checkpoint_path:
                    torch.save(model.state_dict(), checkpoint_path)
            else:
                patience_counter += 1
                if patience_counter >= patience:
                    print(f"Early stopping at epoch {epoch}")
                    break
        
        history['train_loss'].append(loss.item())
    
    return history
```

## Tips for Effective Agent Usage

### 1. Be Specific

**Good**:

> I need a Matérn 5/2 kernel with ARD (different lengthscales per dimension) for 3D coordinates

**Less Effective**:

> I need a kernel

### 2. Provide Context

Include:

- Scientific domain and requirements
- Data characteristics (size, dimensions, constraints)
- Performance requirements (speed, memory, GPU)
- Integration needs (existing code, libraries)

### 3. Specify Quality Requirements

Mention:

- Test coverage expectations
- Numerical stability needs
- Reproducibility requirements
- Documentation standards

### 4. Use Appropriate Agent

- **Multi-phase projects**: Start with Sci-Conductor
- **Quick exploration**: Use Sci-Explore directly
- **Research question**: Use Sci-Research directly
- **Notebook tutorial**: Use Sci-Notebook directly
- **Single figure**: Use Sci-Viz directly

### 5. Review Preservation Documents

After each phase:

- Review decisions made
- Validate assumptions
- Check verifications
- Understand trade-offs

This ensures transparency and helps with future maintenance.

## Getting Help

If agents produce unexpected results:

1. **Check stress-test findings**: Did you address all edge cases?
2. **Review preservation docs**: Were assumptions validated?
3. **Verify environment setup**: Correct Python version, dependencies?
4. **Simplify request**: Break into smaller phases?
5. **Consult README**: Are you using appropriate agent?

For issues or improvements, see the repository issue tracker.
