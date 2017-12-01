def test_1():
    from adventofcode.day1 import solve_captcha

    numbers = [1, 1, 2, 2]

    assert solve_captcha(numbers) == 3


def test_2():
    from adventofcode.day1 import solve_captcha

    numbers = [1, 1, 1, 1]

    assert solve_captcha(numbers) == 4


def test_3():
    from adventofcode.day1 import solve_captcha

    numbers = [1, 2, 3, 4]

    assert solve_captcha(numbers) == 0


def test_4():
    from adventofcode.day1 import solve_captcha

    numbers = [9, 1, 2, 1, 2, 1, 2, 9]

    assert solve_captcha(numbers) == 9
