def test_sum_init():

    from adventofcode2017.day3 import sum_initialisation

    assert sum_initialisation(6) == 10
    assert sum_initialisation(55) == 57
    assert sum_initialisation(120) == 122
    assert sum_initialisation(750) == 806
