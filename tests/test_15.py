def test_a():
    from adventofcode2017.day15 import generator
    gen = generator(f=16807, seed=65)

    assert(next(gen)) == 1092455
    assert(next(gen)) == 1181022009
    assert(next(gen)) == 245556042
    assert(next(gen)) == 1744312007
    assert(next(gen)) == 1352636452


def test_b():
    from adventofcode2017.day15 import generator
    gen = generator(f=48271, seed=8921)

    assert(next(gen)) == 430625591
    assert(next(gen)) == 1233683848
    assert(next(gen)) == 1431495498
    assert(next(gen)) == 137874439
    assert(next(gen)) == 285222916


def test_judge():
    from adventofcode2017.day15 import judge

    assert judge(65, 8921, 5) == 1
