from fnv_hash_fast import fnv1a_32


def test_fnv1a_32():
    assert fnv1a_32(b"hello") == 0x8C959D4E
