# ASCII Shift Cipher 🔐

**Completed:** August 26, 2025

A simple command-line text encoder and decoder written in Python, inspired by Julius Caesar's substitution cipher. Instead of shifting only alphabetic letters, it rotates supported ASCII characters by 13 positions and preserves ordinary spaces.

This project was created as a programming exercise to explore character encoding, loops, and reversible mathematical transformations.

## Features

- **Encryption:** Shift supported non-space characters backward by 13 positions.
- **Decryption:** Reverse the shift to recover the original message.
- **Space preservation:** Keep normal spaces unchanged.
- **ASCII processing:** Convert between characters and numerical values using `ord()` and `chr()`.
- **No external dependencies:** Uses Python's standard functionality only.

## Requirements

- Python 3
- No additional packages required

## Installation and Usage

1. Download or clone the repository.
2. Open a terminal in the folder containing the two Python files.
3. To encrypt a message, run:

   ```bash
   python Main_Encryption_simple.py
   ```

4. Type your message and press Enter. Copy the encoded result.
5. To decode it, run:

   ```bash
   python Main_DeEncryption_simple.py
   ```

6. Paste the encoded message and press Enter.

### Example

```text
Original:  HELLO WORLD
Encrypted: ;8??B JBE?7
Decrypted: HELLO WORLD
```

## How It Works

The programs turn the input string into a list of individual characters and process the characters one by one.

For encryption, each non-space character is converted into its ASCII value and shifted backward with modular arithmetic:

```python
one_letter_encryption = chr((one_letter_ASCII - 13 - 33) % 95 + 33)
```

For decryption, the inverse transformation shifts characters forward:

```python
one_letter_decrypt = chr((one_letter_ASCII + 13 - 33) % 95 + 33)
```

The modulo operator (`%`) wraps values around the 95-character range used by the algorithm. The program treats normal spaces separately, leaving them unchanged.

## Project Structure

```text
ASCII-Shift-Cipher/
├── Main_Encryption_simple.py
├── Main_DeEncryption_simple.py
├── .gitignore
└── README.md
```

## Known Limitations

- **Not secure encryption:** A fixed character shift can easily be reversed. Do not use it for private or sensitive information.
- **ASCII-focused:** Characters outside the supported ASCII range are not reliably processed; Unicode letters such as `č`, `š`, and `ž` are not supported.
- **Non-printing output:** The shift range includes ASCII 127 (DEL), so some encoded output can be difficult to display or copy.
- **Empty and space-only inputs:** The current code prints an error-like message instead of returning an empty or unchanged result.
- **Limited invalid-input handling:** Unsupported characters print an error but do not consistently stop processing.
- **Terminal only:** No graphical interface is included.

## Development Note

I created this project to experiment with the concept of substitution ciphers and to practice Python loops, lists, conditionals, ASCII values, and modular arithmetic. It is intended for learning, not real-world cryptographic security.


**Author:** [Nik Berginc](https://github.com/nikberginc)
