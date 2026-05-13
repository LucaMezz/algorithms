"""Benchmarks for graph algorithms."""

from __future__ import annotations

from benchmarks.cases import BenchmarkCase, BenchmarkSuite, powers_of_two
from benchmarks.complexity import LINEAR, LINEARITHMIC, QUADRATIC

GRAPH_SIZES = powers_of_two(16, 2048)


def path_graph(size: int) -> dict[int, list[int]]:
    """Return an undirected path graph with size vertices."""
    graph: dict[int, list[int]] = {vertex: [] for vertex in range(size)}
    for vertex in range(size - 1):
        graph[vertex].append(vertex + 1)
        graph[vertex + 1].append(vertex)
    return graph


SUITE = BenchmarkSuite(
    name="graphs",
    cases=(
        # Example for future use:
        # BenchmarkCase(
        #     name="breadth_first_search path graph",
        #     input_factory=path_graph,
        #     operation=lambda graph: breadth_first_search(graph, source=0),
        #     sizes=GRAPH_SIZES,
        #     expected_time=LINEAR,  # O(V + E), and E ~= V for path graphs
        #     expected_space=LINEAR,
        # ),
    ),
)

__all__ = [
    "GRAPH_SIZES",
    "LINEAR",
    "LINEARITHMIC",
    "QUADRATIC",
    "SUITE",
    "BenchmarkCase",
    "BenchmarkSuite",
    "path_graph",
]
