Kernel Guide
============

This guide introduces :class:`dummy_gp.kernels.ExponentialKernel` and
:func:`dummy_gp.kernels.normalize_coordinates` for simple one-dimensional
Gaussian process examples.

When to use this sandbox API
----------------------------

Use the sandbox when you need a compact example of a stationary covariance model
without additional dependencies. The implementation is intentionally small and
best suited to documentation examples, tests, and teaching material.

The kernel assumes:

* scalar one-dimensional coordinates,
* a strictly positive lengthscale,
* a strictly positive variance, and
* dense covariance matrices represented as Python lists.

Normalizing coordinates
-----------------------

The helper :func:`dummy_gp.kernels.normalize_coordinates` shifts a sequence of
coordinates so the smallest value becomes a chosen offset.

.. code-block:: python

	from dummy_gp import normalize_coordinates

	raw_points = [10.5, 11.0, 12.25]
	shifted_points = normalize_coordinates(raw_points)
	anchored_points = normalize_coordinates(raw_points, offset=1.0)

``shifted_points`` becomes ``[0.0, 0.5, 1.75]`` and preserves the original
spacing. This is useful when you want examples with a clean origin but do not
want to change the effective distance scale.

Evaluating pairwise covariance
------------------------------

Instantiate :class:`dummy_gp.kernels.ExponentialKernel` with a positive
lengthscale and variance.

.. code-block:: python

	from dummy_gp import ExponentialKernel

	kernel = ExponentialKernel(lengthscale=2.0, variance=1.5)
	k_same = kernel(0.0, 0.0)
	k_nearby = kernel(0.0, 1.0)

The diagonal value ``k_same`` equals the variance. Covariance decays
exponentially as the distance between coordinates increases.

Building a covariance matrix
----------------------------

Use :meth:`dummy_gp.kernels.ExponentialKernel.covariance_matrix` to evaluate the
kernel on a list of coordinates.

.. code-block:: python

	points = [0.0, 0.5, 1.5]
	matrix = kernel.covariance_matrix(points)

The returned matrix is symmetric and square, with one row and column per input
point. Because the implementation uses nested Python loops, it is intended for
small examples rather than large numerical workloads.

Limitations
-----------

This sandbox package is intentionally narrow in scope:

* it does not support multidimensional coordinates,
* it does not integrate with NumPy, SciPy, or GPU-backed tensors, and
* it does not add jitter or other stabilization terms for ill-conditioned
  covariance matrices.

For production Gaussian process models, treat this package as illustrative
documentation material rather than as a full numerical toolkit.
