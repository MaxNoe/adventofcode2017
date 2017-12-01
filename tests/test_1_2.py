def test_1():
    from adventofcode2017.day1 import solve_captcha_2

    numbers = [1, 2, 1, 2]

    assert solve_captcha_2(numbers) == 6


def test_2():
    from adventofcode2017.day1 import solve_captcha_2

    numbers = [1, 2, 2, 1]

    assert solve_captcha_2(numbers) == 0


def test_3():
    from adventofcode2017.day1 import solve_captcha_2

    numbers = [1, 2, 3, 4, 2, 5]

    assert solve_captcha_2(numbers) == 4


def test_4():
    from adventofcode2017.day1 import solve_captcha_2

    numbers = [1, 2, 3, 1, 2, 3]

    assert solve_captcha_2(numbers) == 12


def test_4():
    from adventofcode2017.day1 import solve_captcha_2

    numbers = [1, 2, 1, 3, 1, 4, 1, 5]

    assert solve_captcha_2(numbers) == 4
