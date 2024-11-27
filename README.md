# Text Processing Utilities

## Overview

This repository contains two Python scripts developed for COMP-375 (Computer Security) that provide text processing capabilities:

1. **Substitution Cipher Encryption/Decryption**
2. **Letter Frequency Analyzer**

## Scripts

### 1. Substitution Cipher Encryption/Decryption

#### Features

- Encrypt and decrypt text using a substitution cipher
- Read encryption/decryption key from a file
- Process input text files
- Generate output files with encrypted or decrypted text

#### Usage

```bash
$ python substitution_cipher.py
Enter 'encrypt' or 'decrypt': encrypt
Enter the name of the key file: key.txt
Enter the name of the input file: input.txt
Operation completed. Result written to encrypted-text.txt
```

#### Key File Format

The key file should contain character mappings. The script uses the second column to build the substitution key.

### 2. Letter Frequency Analyzer

#### Features

- Read text file contents
- Calculate frequency of each letter
- Sort letter frequencies in descending order
- Generate output file with frequency statistics

#### Usage

```bash
$ python letter_frequency.py
Enter the text file name: sample.txt
Letter frequencies written to letter_frequencies.txt
```

#### Output Format

The `letter_frequencies.txt` file contains:

- Each letter found in the text
- Number of times the letter appears
- Sorted from most frequent to least frequent

## Requirements

- Python 3.x
- Input text files
- (Optional) Key file for encryption/decryption

## Example Output

### Substitution Cipher

- Output files: `encrypted-text.txt` or `decrypted-text.txt`

### Letter Frequency Analyzer

Sample `letter_frequencies.txt`:

```
e: 45
t: 32
a: 28
...
```

## Author

**Sayed Abdul Ahad Ibrahimi**

- Date: 09/10/2023
- Course: COMP-375 (Computer Security)
