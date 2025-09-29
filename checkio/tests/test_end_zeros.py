from end_zeros import end_zeros


def test_end_zeros():
    assert end_zeros(0) == 1
    assert end_zeros(100100) == 2
    assert end_zeros(100) == 2
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100100) == 2