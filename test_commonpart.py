from commonpart import common_parts, random_list


def test1_common_parts():
    assert common_parts([1,1,3,4,5,5,6],[5]) == {5}

def test2_random_list():
    assert type(random_list()) is list
