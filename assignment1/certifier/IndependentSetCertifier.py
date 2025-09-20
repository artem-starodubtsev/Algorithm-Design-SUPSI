from dataclasses import dataclass

from .core.Certifier import Certifier
from .core.Graph import Graph


@dataclass
class IndependentSetInstance:
    G: Graph


@dataclass
class IndependentSetSolution:
    vertices: list[int]


class IndependentSetCertifier(Certifier[IndependentSetInstance, IndependentSetSolution]):
    def certify(self, instance: IndependentSetInstance, solution: IndependentSetSolution) -> bool:
        for i in range(len(solution.vertices)):
            for j in range(i + 1, len(solution.vertices)):
                if instance.G.has_edge(solution.vertices[i], solution.vertices[j]) or instance.G.has_edge(
                        solution.vertices[j], solution.vertices[i]):
                    return False
        return True
