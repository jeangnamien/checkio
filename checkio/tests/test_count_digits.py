from count_digits import count_digits   

def test_count_digits():
    assert count_digits("There are 2 apples") == 1
    assert count_digits("123456") == 6
    assert count_digits("This is the 1st test") == 1
    assert count_digits("This is a test 1") == 1
    assert count_digits("This is a test 12") == 2
    assert count_digits("") == 0