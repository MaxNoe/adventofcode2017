def test_1():
    from adventofcode2017.day4 import is_valid_password

    assert is_valid_password('aa bb cc dd ee')
    assert not is_valid_password('aa bb cc dd aa')
    assert is_valid_password('aa bb cc dd aaa')
