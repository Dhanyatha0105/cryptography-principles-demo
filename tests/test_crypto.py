"""Round-trip and integrity tests for the cryptography demos."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from integrity_demo import sha256_hex, verify  # noqa: E402


def test_sha256_known_vector():
    # SHA-256 of empty string
    assert sha256_hex(b"") == (
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )


def test_verify_detects_tampering():
    original = b"Transfer 1000 to account 4471."
    tampered = b"Transfer 9000 to account 4471."
    assert verify(original, original) is True
    assert verify(original, tampered) is False


def test_avalanche_effect():
    a = sha256_hex(b"hello")
    b = sha256_hex(b"hellp")  # one character changed
    assert a != b
    assert len(a) == len(b) == 64


if __name__ == "__main__":
    test_sha256_known_vector()
    test_verify_detects_tampering()
    test_avalanche_effect()
    print("All tests passed.")
