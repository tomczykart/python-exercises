from birthday import calculate_when

def test_1_birthday():
    assert calculate_when(22) == 2100

def test_2_birthday():
    assert calculate_when(100) == 2022
