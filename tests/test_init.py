from fnvhash import fnv1a_32 as fnvhash_fnv1a_32

from fnv_hash_fast import fnv1a_32


def test_fnv1a_32():
    assert fnv1a_32(b"hello") == 1335831723
    assert fnv1a_32(b"goodbye") == 1188507472
    assert fnv1a_32(b"goodbye" * 4096) == 386067909


def test_fnvhash_fnv1a_32():
    for test_data in (
        b"hello",
        b"goodbye",
        b"goodbye" * 4096,
    ):
        assert fnv1a_32(test_data) == fnvhash_fnv1a_32(test_data)
