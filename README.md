# Cryptography Principles Demonstration

A hands-on demonstration of two core principles of modern cryptography:
**Confidentiality** (encryption) and **Integrity** (hashing). Both are
implemented from first principles in pure Python with no external dependencies.

---

## 1. Confidentiality — Speck 32/64 Block Cipher

`speck_cipher.py` is a from-scratch implementation of the **Speck 32/64**
lightweight block cipher (an ARX design — Add, Rotate, XOR).

It implements:

- `speck_key_schedule` — derives the 22 round keys from the master key
- `speck_encrypt` — encrypts a 32-bit block
- `speck_decrypt` — inverts the round function to recover the plaintext

Running the script encrypts a sample plaintext and then decrypts the
ciphertext, proving the original message is recovered exactly.

```bash
python speck_cipher.py
```

## 2. Integrity — SHA-256 Hashing

`integrity_demo.py` shows how a cryptographic hash detects tampering. It hashes
a message, then hashes a copy with a single character changed, and shows that
the two digests are completely different — the avalanche property.

```bash
python integrity_demo.py
```

Example output:

```
Case 1 - identical copy:        digest matches? True
Case 2 - one character changed: digest matches? False
```

A one-character change ("1000" → "9000") yields an entirely different digest,
so any modification to the data is immediately detectable.

---

## Why these two?

Together they cover two of the three pillars of information security:

| Principle        | Guarantees                          | Demonstrated by    |
|------------------|-------------------------------------|--------------------|
| Confidentiality  | Only authorized parties can read it | Speck cipher       |
| Integrity        | Data has not been altered           | SHA-256 hashing    |

## Requirements

Python 3.8+ — standard library only.
