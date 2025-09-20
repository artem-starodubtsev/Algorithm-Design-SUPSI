from dataclasses import dataclass

from .core.Certifier import Certifier
from .core.Graph import Graph


@dataclass
class BipartiteMatchingInstance:
    G: Graph


@dataclass
class BipartiteMatchingSolution:
    vertices_pairs: list[tuple[int, int]]


class BipartiteMatchingCertifier(Certifier[BipartiteMatchingInstance, BipartiteMatchingSolution]):
    def certify(self, instance: BipartiteMatchingInstance, solution: BipartiteMatchingSolution) -> bool:
        seen = set()
        for v1, v2 in solution.vertices_pairs:
            if v1 in seen or v2 in seen or not instance.G.has_edge(v1, v2):
                return False
            seen.add(v1)
            seen.add(v2)

        return True
