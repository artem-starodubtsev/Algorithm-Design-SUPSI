from assignment1.certifier import *


if __name__ == "__main__":

    mapping = ["A", "B", "C", "D"]
    M = [
        [False, True,  False, False],
        [True,  False, True,  False],
        [False, True,  False, True ],
        [False, False, True,  False],
    ]
    graph = Graph.from_matrix(mapping, M)

    instance = IndependentSetInstance(graph)
    good_set  = IndependentSetSolution([0, 2])
    bad_set = IndependentSetSolution([1, 2])

    print(IndependentSetCertifier().certify(instance, good_set))
    print(IndependentSetCertifier().certify(instance, bad_set))
