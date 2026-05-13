"""Expected complexity curves used by benchmark plots."""

from __future__ import annotations

from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from math import log2

CurveFunction = Callable[[int], float]


@dataclass(frozen=True)
class ComplexityModel:
    """A named complexity curve that can be compared with measurements."""

    name: str
    function: CurveFunction

    def values(self, sizes: Iterable[int]) -> list[float]:
        """Return raw curve values for input sizes."""
        return [self.function(size) for size in sizes]


def _positive(size: int) -> int:
    return max(size, 1)


CONSTANT = ComplexityModel("O(1)", lambda size: 1.0)
LOGARITHMIC = ComplexityModel("O(log n)", lambda size: log2(max(size, 2)))
LINEAR = ComplexityModel("O(n)", lambda size: float(_positive(size)))
LINEARITHMIC = ComplexityModel(
    "O(n log n)",
    lambda size: float(_positive(size)) * log2(max(size, 2)),
)
QUADRATIC = ComplexityModel("O(n^2)", lambda size: float(_positive(size) ** 2))
CUBIC = ComplexityModel("O(n^3)", lambda size: float(_positive(size) ** 3))

MODELS_BY_NAME: dict[str, ComplexityModel] = {
    model.name: model
    for model in (
        CONSTANT,
        LOGARITHMIC,
        LINEAR,
        LINEARITHMIC,
        QUADRATIC,
        CUBIC,
    )
}


def normalized_curve(
    model: ComplexityModel,
    sizes: Sequence[int],
    observed_values: Sequence[float],
) -> list[float]:
    """Scale a theoretical curve so it can be overlaid on observed data.

    The final non-zero observation is used as the anchor. This keeps plots easy
    to read while preserving the expected shape of the complexity curve.
    """
    if len(sizes) != len(observed_values):
        msg = "sizes and observed_values must have the same length"
        raise ValueError(msg)

    raw_values = model.values(sizes)
    if not raw_values:
        return []

    anchor_index = _find_anchor_index(raw_values, observed_values)
    if anchor_index is None:
        return [0.0 for _ in raw_values]

    raw_anchor = raw_values[anchor_index]
    observed_anchor = observed_values[anchor_index]
    if raw_anchor == 0:
        return [0.0 for _ in raw_values]

    scale = observed_anchor / raw_anchor
    return [raw_value * scale for raw_value in raw_values]


def _find_anchor_index(
    raw_values: Sequence[float],
    observed_values: Sequence[float],
) -> int | None:
    for index in range(len(observed_values) - 1, -1, -1):
        if raw_values[index] > 0 and observed_values[index] > 0:
            return index
    return None

