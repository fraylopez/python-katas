

def test_fizzbuzz_of_3_returns_fizz():
    assert fizzbuzz(3) == "fizz"

def test_fizzbuzz_of_5_returns_buzz():
    assert fizzbuzz(5) == "buzz"

def test_fizzbuzz_of_15_returns_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"


def test_fizzbuzz_till_5():
    assert fizzbuzz_till_n(5) == ["1", "2", "fizz", "4", "buzz"]

def test_fizzbuzz_till_15():
    assert fizzbuzz_till_n(15) == ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz"]

def test_fizzbuzz_till_0():
  assert fizzbuzz_till_n(0) == []



def fizzbuzz_till_n(n):
    return [fizzbuzz(i) for i in range(1, n+1)]

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"

    if number % 3 == 0:
        return "fizz"

    if number % 5 == 0:
        return "buzz"


    return str(number)