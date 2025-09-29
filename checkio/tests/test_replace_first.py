from replace_first import replace_first

def test_replace_first():
    assert replace_first([1, 2, 3, 4, 5]) == [2, 3, 4, 5, 1]
    assert replace_first([1, 2]) == [2, 1]
    assert replace_first([1]) == [1]
    assert replace_first([]) == []
    assert replace_first([True, False, False]) == [False, False, True]
    assert replace_first(["first", "second", "third"]) == [ "second", "third", "first"]