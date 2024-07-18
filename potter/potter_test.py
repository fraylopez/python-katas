from potter import calculate_price


def test_basics():
    assert calculate_price([]) == 0
    assert calculate_price([1]) == 8
    assert calculate_price([1, 1]) == 16
    assert calculate_price([1, 2]) == 15.2
    assert calculate_price([1, 2, 3]) == 21.6
    assert calculate_price([1, 2, 3, 4]) == 25.6
    assert calculate_price([1, 2, 3, 4, 5]) == 30


def test_two_different_and_some_repeated_books():
    assert calculate_price([1, 2, 2]) == 23.2
    assert calculate_price([1, 2, 3, 3, 3]) == 37.6


def test_sets():
    assert calculate_price([1, 2, 1, 2]) == 30.4
    assert calculate_price([1, 2, 1, 2, 3]) == 37.6
    assert calculate_price([1, 2, 2, 3, 4, 5]) == 38
    assert calculate_price([1, 1, 2, 2, 3, 3, 4, 5]) == 51.2


def test_no_sets():
    assert calculate_price([1, 2, 2, 2]) == 31.2
