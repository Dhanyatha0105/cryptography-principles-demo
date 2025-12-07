"""
Integrity demonstration using SHA-256.

A cryptographic hash produces a fixed-length fingerprint of some data. If even a
single byte of the input changes, the resulting digest changes completely. This
property lets us detect tampering or corruption.

Run:
    python integrity_demo.py
"""

import hashlib


def sha256_hex(data: bytes) -> str:
    """Return the hex SHA-256 digest of the given bytes."""
    return hashlib.sha256(data).hexdigest()


def verify(original: bytes, received: bytes) -> bool:
    """Return True if the received data matches the original digest."""
    return sha256_hex(original) == sha256_hex(received)


def main() -> None:
    message = b"Transfer 1000 to account 4471."
    tampered = b"Transfer 9000 to account 4471."

    original_hash = sha256_hex(message)
    print(f"Original message : {message.decode()}")
    print(f"SHA-256 digest   : {original_hash}\n")

    print("Case 1 - identical copy:")
    intact = message
    print(f"  digest matches? {verify(message, intact)}  "
          f"({sha256_hex(intact)})\n")

    print("Case 2 - one character changed (1000 -> 9000):")
    print(f"  digest matches? {verify(message, tampered)}  "
          f"({sha256_hex(tampered)})")
    print("\nA single-character change produces a completely different digest,")
    print("so any tampering is immediately detectable.")


if __name__ == "__main__":
    main()
