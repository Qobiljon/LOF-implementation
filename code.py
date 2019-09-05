# -*- coding: utf8 -*-
import lof

instances = (
    (1.2, 1.6, 2.5),
    (2.5, 2.8, 3.1),
    (3.0, 3.0, 10.5),
    (2.8, 1.8, 0.8),
    (1.1, 2.3, 1.8),
    (5.8, 6.7, 2.1)
)
instance = (1.2, 1.3, 1.1)


def test_lof_normalize_instances():
    l = lof.LOF(((1, 1), (2, 2)), normalize=True)
    assert l.instances == [(0.0, 0.0), (1.0, 1.0)]
    l = lof.LOF(((1, 1), (2, 2), (3, 3)), normalize=True)
    assert l.instances == [(0.0, 0.0), (0.5, 0.5), (1.0, 1.0)]


def test_distance():
    assert 1 == lof.distance_euclidean((1, 1), (2, 2))


def test_k_distance():
    instances = ((1, 1), (2, 2), (3, 3))
    d = lof.k_distance(1, (2, 2), instances)
    assert d == (0.0, [(2, 2)])
    d = lof.k_distance(1, (2.2, 2.2), instances)
    assert d == (0.20000000000000018, [(2, 2)])
    d = lof.k_distance(1, (2.5, 2.5), instances)
    assert d == (0.5, [(2, 2), (3, 3)])
    d = lof.k_distance(5, (2.2, 2.2), instances)
    assert d == (1.2000000000000002, [(2, 2), (3, 3), (1, 1)])


def test_reach_distance():
    instances = ((1, 1), (2, 2), (3, 3))
    lof.k_reach_distance(1, (1, 1), (2, 2), instances)


def test_outliers():
    print(lof.outliers(3, instances))


def test_normalization_problems():
    # see issue https://github.com/damjankuznar/pylof/issues/7
    instances = [(1., 2., 3.), (2., 3., 4.), (1., 2., 4.), (1., 2., 1.)]
    l = lof.outliers(1, instances)


def test_duplicate_instances():
    instances = (
        (1, 1, 1, 1),
        (2, 2, 2, 2),
        (3, 3, 3, 3),
        (2, 1, 1, 1),
        (1, 2, 1, 1),
        (2, 2, 2, 2),
        (2, 2, 2, 2),
        (1, 1, 1, 1),
        (1, 1, 1, 1),
        (13, 13, 13, 13)
    )
    lof.outliers(1, instances)


if __name__ == "__main__":
    print("Running tests, nothing more should appear if everything goes well.")
    test_lof_normalize_instances()
    test_distance()
    test_k_distance()
    test_reach_distance()
    test_outliers()
    test_normalization_problems()
