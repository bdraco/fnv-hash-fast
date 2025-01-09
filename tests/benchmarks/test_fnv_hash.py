from pytest_codspeed import BenchmarkFixture

from fnv_hash_fast import fnv1a_32


def test_fnv1a_32(benchmark: BenchmarkFixture) -> None:
    @benchmark
    def test_fnv1a_32() -> None:
        fnv1a_32(b"hello")


def test_fnv1a_32_large_payload(benchmark: BenchmarkFixture) -> None:
    payload = b"goodbye" * 4096

    @benchmark
    def test_fnv1a_32_large_payload() -> None:
        fnv1a_32(payload)
