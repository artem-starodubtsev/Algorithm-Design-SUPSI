from dataclasses import dataclass


@dataclass
class Graph[T]:
    _vertices: list[T]
    _edges: dict[int, frozenset[int]]

    @staticmethod
    def from_matrix(mapping: list[T], matrix: list[list[bool]]) -> "Graph[T]":
        assert len(matrix) == len(matrix[0]) and len(matrix) == len(mapping)

        n = len(mapping)
        edges: dict[int, frozenset[int]] = {
            i: frozenset(
                j for j in range(n)
                if i != j and matrix[i][j]
            )
            for i in range(n)
        }
        return Graph(mapping, edges)

    @property
    def vertices(self) -> list[T]:
        return self._vertices

    @property
    def edges(self) -> dict[int, frozenset[int]]:
        return self._edges

    def has_edge(self, i: int, j: int) -> bool:
        return j in self._edges.get(i, frozenset())
