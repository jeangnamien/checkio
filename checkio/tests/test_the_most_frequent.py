from the_most_frequent import most_frequent


def test_most_frequent():
    assert most_frequent([1, 1, 2, 2, 3]) == 1
    assert most_frequent([3, 3, 1, 3, 2, 1, 2, 3]) == 3
    assert most_frequent([1]) == 1
    assert most_frequent([0, 0, 0.1, 0.1]) == 0
    