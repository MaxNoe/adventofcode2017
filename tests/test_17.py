def test_insertion():
    from adventofcode2017.day17 import build_ring_buffer

    assert build_ring_buffer(size=1, steps=3) == [0]
    assert build_ring_buffer(size=2, steps=3) == [0, 1]
    assert build_ring_buffer(size=3, steps=3) == [0, 2, 1]
    assert build_ring_buffer(size=4, steps=3) == [0, 2, 3, 1]
    assert build_ring_buffer(size=5, steps=3) == [0, 2, 4, 3, 1]
    assert build_ring_buffer(size=6, steps=3) == [0, 5, 2, 4, 3, 1]

    buf = build_ring_buffer(2018, 3)
    idx = buf.index(2017)
    assert buf[idx + 1] == 638
