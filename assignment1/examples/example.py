from assignment1.certifier import *
from assignment1.certifier import BipartiteMatchingInstance

if __name__ == "__main__":
    # IndependentSet check
    mapping = ["A", "B", "C", "D"]
    M = [
        [False, True, False, False],
        [True, False, True, False],
        [False, True, False, True],
        [False, False, True, False],
    ]
    graph = Graph.from_matrix(mapping, M)

    instance = IndependentSetInstance(graph)
    good_set = IndependentSetSolution([0, 2])
    bad_set = IndependentSetSolution([1, 2])

    print(IndependentSetCertifier().certify(instance, good_set))
    print(IndependentSetCertifier().certify(instance, bad_set))
    print('-' * 50)

    # IntervalScheduling check
    S = Schedule.from_tuples([
        (0, 6),
        (1, 4),
        (3, 5),
        (3, 8),
        (4, 7),
        (5, 9),
        (6, 10),
        (8, 11),
    ])

    instance = IntervalSchedulingInstance(S)

    good_set = IntervalSchedulingSolution(interval_idxes=[1, 4, 7])
    bad_set = IntervalSchedulingSolution(interval_idxes=[0, 5])

    print(IntervalSchedulingCertifier().certify(instance, good_set))
    print(IntervalSchedulingCertifier().certify(instance, bad_set))
    print("-" * 50)

    #  BipartiteMatching check
    mapping = ["A", "B", "C", "D"]
    M = [
        [False, True, False, False],
        [True, False, True, False],
        [False, True, False, True],
        [False, False, True, False],
    ]
    graph = Graph.from_matrix(mapping, M)

    instance = BipartiteMatchingInstance(graph)
    good_set = BipartiteMatchingSolution([(0, 1), (2, 3)])
    bad_set = BipartiteMatchingSolution([(0, 2), (3, 1)])

    print(BipartiteMatchingCertifier().certify(instance, good_set))
    print(BipartiteMatchingCertifier().certify(instance, bad_set))
    print('-' * 50)
