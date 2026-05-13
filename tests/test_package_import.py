"""Tests for basic package import behavior."""

import algorithms


def test_package_imports() -> None:
    """The algorithms package should be importable."""
    assert algorithms is not None
