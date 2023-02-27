# Secret_Decoder_Ring

This program is designed to allow users to encrypt and decrypt messages using different encryption methods in Python. It uses two encryption techniques, the Atbash Cipher and the Caesar Cipher. The program implements a class structure using inheritance. The Cipher class is the parent class of both the AtbashCipher and CaesarCipher classes. The AtbashCipher class overrides the methods of the parent Cipher class to implement the Atbash Cipher encryption algorithm.

## Features:
- Allows users to encrypt and decrypt messages using the Atbash Cipher and Caesar Cipher.
- Implements a class structure using inheritance.
- Allows user input via the console.
- Can write encrypted messages to a file named 'message.txt'.
- Can read and decrypt messages from 'message.txt' and display them to the console.
- Handles non-letter characters and preserves their original placement in the message during encryption and decryption.
- Supports upper and lower case letters in the messages.
