from sum_numbers import sum_numbers


def test_sum_numbers():
    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0