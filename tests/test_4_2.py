def test_1():

    from adventofcode2017.day4 import is_valid_password

    assert is_valid_password('abcde fghij', anagrams=False)

    assert not is_valid_password('abcde xyz ecdab', anagrams=False)
    assert is_valid_password('a ab abc abd abf abj', anagrams=False)
    assert is_valid_password('iiii oiii ooii oooi oooo', anagrams=False)
    assert not is_valid_password('oiii ioii iioi iiio', anagrams=False)
