from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], 5, "test") == "test"
    assert arrs.get([1, 2, 3], 3, "test") == "test"



def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

    # ѕровер€ем случай, когда не указаны границы среза
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]

    # ѕровер€ем случай, когда начальный индекс отрицателен
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]

    # ѕровер€ем случай, когда конечный индекс отрицателен
    assert arrs.my_slice([1, 2, 3, 4], end=-1) == [1, 2, 3]

    # ѕровер€ем случай, когда не указаны границы среза (оба индекса None)
    assert arrs.my_slice([1, 2, 3, 4], None, None) == [1, 2, 3, 4]

    # ѕровер€ем случай, когда оба индекса отрицательны
    assert arrs.my_slice([1, 2, 3, 4], -2, -1) == [3]

    # ѕровер€ем случай, когда начальный индекс равен 0
    assert arrs.my_slice([1, 2, 3, 4], 0, 2) == [1, 2]

    # ѕровер€ем случай, когда конечный индекс равен 0
    assert arrs.my_slice([1, 2, 3, 4], 1, 0) == []

    assert arrs.my_slice([]) == []