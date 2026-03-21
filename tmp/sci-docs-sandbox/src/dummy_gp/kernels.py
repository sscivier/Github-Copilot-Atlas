"""Small Gaussian process kernel utilities used in the docs sandbox.

The module intentionally stays small so documentation workflows can focus on
API clarity, cross-references, and Sphinx wiring rather than on a large runtime
surface. The public API covers one preprocessing helper and one stationary
kernel for 1D coordinates.
"""

from __future__ import annotations

from math import exp


def normalize_coordinates(points: list[float], offset: float = 0.0) -> list[float]:
    """Translate coordinates so the smallest value becomes ``offset``.

    Normalizing coordinates can make examples easier to read because the first
    point starts at a predictable origin while preserving all pairwise
    distances.

    :param points: One-dimensional coordinates in observation order.
    :param offset: Value assigned to the smallest coordinate after shifting.
    :returns: Shifted coordinates with the same spacing as ``points``.

    .. note::

       The function only translates the inputs. It does not rescale them, so
       any physical unit associated with the coordinates is preserved.
    """
    if not points:
        return []

    minimum = min(points)
    return [point - minimum + offset for point in points]


class ExponentialKernel:
    """Exponential covariance kernel for one-dimensional coordinates.

    Covariance decays exponentially with the absolute distance between two
    coordinates. The ``variance`` parameter sets the covariance at zero
    separation, while ``lengthscale`` controls how quickly correlation drops as
    points move apart. The implementation assumes scalar 1D inputs and returns
    dense Python lists for simplicity.

    :param lengthscale: Positive correlation length in the same units as the
        input coordinates.
    :param variance: Positive marginal variance.
    :raises ValueError: If either parameter is not strictly positive.

    .. note::

       This sandbox implementation is intentionally minimal. It does not handle
       vectorized NumPy arrays, batching, or numerical stabilization for large
       matrices.
    """

    def __init__(self, lengthscale: float, variance: float = 1.0) -> None:
        """Initialize the kernel with positive scale parameters."""
        if lengthscale <= 0:
            raise ValueError("lengthscale must be positive")
        if variance <= 0:
            raise ValueError("variance must be positive")

        self.lengthscale = lengthscale
        self.variance = variance

    def __call__(self, x1: float, x2: float) -> float:
        """Evaluate the covariance between two scalar coordinates.

        :param x1: First coordinate.
        :param x2: Second coordinate.
        :returns: Covariance implied by the exponential kernel.
        """
        distance = abs(x1 - x2)
        return self.variance * exp(-distance / self.lengthscale)

    def covariance_matrix(self, points: list[float]) -> list[list[float]]:
        """Construct a dense covariance matrix for a sequence of points.

        :param points: One-dimensional coordinates ordered as observations.
        :returns: Square covariance matrix stored as nested Python lists.

        .. note::

           An empty input returns an empty matrix. The method performs a direct
           nested-loop evaluation, so the cost grows quadratically with the
           number of points.
        """
        return [[self(point_i, point_j) for point_j in points] for point_i in points]
