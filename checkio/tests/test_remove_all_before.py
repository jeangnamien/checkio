from remove_all_before import remove_all_before 


def test_remove_all_before():
    assert remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert remove_all_before([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
    assert remove_all_before([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert remove_all_before([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]
    assert remove_all_before([], 0) == []