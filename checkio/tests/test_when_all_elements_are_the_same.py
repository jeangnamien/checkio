from all_the_same import all_the_same

def test_all_the_same():
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False