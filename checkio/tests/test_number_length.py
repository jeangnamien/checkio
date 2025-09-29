from number_length import number_length


def test_number_length():
    assert number_length(4) == 1
    assert number_length(44) == 2
    assert number_length(444444444) == 9
    assert number_length(4444444444) == 10
    assert number_length(0) == 1