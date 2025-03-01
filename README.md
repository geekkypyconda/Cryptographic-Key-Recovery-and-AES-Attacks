# Cryptographic-Key-Recovery-and-AES-Attacks

# Cryptographic-Key-Recovery
=====================================

## Overview

This involves decrypting cipher texts using a cryptanalysis technique. The main file that contains the hardcoded key is `cs23mtech11005_DecryptCipherTexts.py`. To get the messages and the key, execute this file.

## Procedure
-------------

### Step 1: CPAS_Tester.py

In this file, I used the following logic:

#### Logic

A. Read all cipher texts from `streamciphertexts.txt` and store them in a list.
B. Convert all cipher texts from hexadecimal strings to integer lists.
C. XOR all cipher texts with each other.
D. For every pair of XORed cipher texts, check if the result lies in the range of alphabet characters. If not, skip this position. If it does, use the following strategy:
   * If the XOR result is an uppercase character, there can be multiple possibilities. One possibility is that `m1` is a space and `m2` is a small character. Use the equation `m1 - XOR - c1 = m2 - XOR - c2 = key` to fill in the values and check if the equation holds. If it does, update the messages and key at that index. If not, swap the values of `m1` and `m2` and check again. If it still doesn't hold, skip this index.
E. After applying this strategy, get a key in bits and pieces. Then, XOR all cipher texts with the key to get the messages in bits and pieces.
F. Store the messages (in bits and pieces) in a file named `brokenMessages.txt`.

### Step 2: Decoding Messages

Copy the broken text from `brokenMessages.txt` to another file `decodingMessages.txt`. Then, try to guess some of the text using spaces and make changes in the file `decodingMessages.txt`. Run the file `CPAS_Checker.py`.

#### Logic

A. Copy all messages in `decodingMessages.txt` into a list and all cipher texts into another list.
B. XOR the last broken message with the last cipher text to get a partial key.
C. XOR all other cipher texts with the partial key and print the messages.
D. The messages are now slightly improved compared to the previous ones.
E. Copy the messages back into `decodingMessages.txt`.
F. Repeat the procedure until all messages are correct.

### Step 3: Confirmation

After repeating the procedure, it confirms that the key obtained by XORing the last message and last cipher text is correct.

### Step 4: Final Decryption

Hardcode the key in `cs23mtech11005_DecryptCipherTexts.py` and XOR all cipher texts with the key to print the messages and the key.

---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------

# AES Attacks

## Attack 1: Short Key Brute Force

## How to Run the Program
-------------------------

### Steps

1. Run the file "cs23mtech11005_A.py" to get the key and the special message.
2. This program uses a brute force attack by trying all possible keys to find the exact key.
3. Once the key is found, it is used to crack the special message.

### Other Mentions
-----------------

* The file "aesLongKeyGen24.py" is used to expand the key.
* The program reads from the files "aesCiphertexts.txt" and "aesPlaintexts.txt".
* The special message is written to the file "aesSecretMessage.txt".

## Attack 2: Meet in the Middle Attack

## How to Run the Program
-------------------------

### Steps

1. Run the file "cs23mtech11005_B.py" to get the key pair and the special message.
2. This program uses a Meet in the Middle attack by encrypting from one side and decrypting from the other side, and then comparing to find the key pair.
3. Once the key pair is found, it is used to find the secret message.

### Other Mentions
-----------------

* The file "2aesLongKeyGen16.py" is used to expand the key.
* The program reads from the files "2aesCiphertexts.txt" and "2aesPlaintexts.txt".
* The special message is written to the file "2aesSecretMessage.txt".

