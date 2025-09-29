from all_upper import is_all_upper

def test_all_upper():
    assert is_all_upper("ALL UPPER") == True
    assert is_all_upper("all lower") == False
    assert is_all_upper("mixed UPPER and lower") == False
    assert is_all_upper("12345") == True
    assert is_all_upper("") == True