# cryptocoder-XOR_8bit

Introduction:
Crypto coder is a basic encryption and decryption algorithm implemented in Python. It employs the XOR (exclusive OR) operation with an 8-bit key to encrypt and decrypt messages. The encryption process takes a plaintext message and applies bitwise XOR between each character of the message and the key. Similarly, decryption is performed by XORing the encrypted message with the same key.

This project has two main functions:
•	Encrypt (message, key): This function takes a plaintext message and an 8-bit key as input. It iterates over each character in the message and performs the XOR operation between the character and the key. The result is an encrypted message where each character is transformed using the key.
•	Decrypt (encrypted message, key): This function performs the reverse operation of the encrypt function. It takes an encrypted message and the same key used for encryption. By XORing each character of the encrypted message with the key, the original plaintext is recovered.

This project also includes additional functions to read plaintext from a .txt file, encrypt or decrypt the message, and save the results to .txt files. By running the “Python crypto_coder.py” in the terminal, you can encrypt a plaintext message stored in a file, save the encrypted message to another file, and then decrypt the encrypted message back to the original plaintext, saving it in a separate file.


How to run?
To run this project, save your plaintext message in a file called "plaintext.txt". When you run the code in cryptyo_coder.py using “Python crypto_coder.py” in the terminal, it will encrypt the message using the specified encryption key (we set it to, 127) and save the encrypted message to "encrypted.txt". Then, it will decrypt the encrypted message and save the decrypted message to "decrypted.txt".

After running the code, you will see two new files generated:
•	encrypted.txt: This file contains the encrypted version of the plaintext message.
•	decrypted.txt: This file contains the decrypted version of the encrypted message.

When encrypting or decrypting, the extracted key is used in the XOR operation as before. It reads the plaintext from the file and automatically extracts the encryption key from it. Similarly, when decrypting, the code reads the encrypted message and extracts the encryption key from it.

Algorithm used: 
The XOR method is used in this project to perform a simple form of encryption and decryption. The XOR (Exclusive OR) is a bitwise operation that combines two binary values, where each bit in the result is set if and only if exactly one of the corresponding bits in the operands is set. In this project, XOR is used to alter the binary representation of each character in the message using a key. 
How it works:
Encryption:
•	Each character in the message is converted to its corresponding ASCII value.
•	The ASCII value of the character is XORed with the key using the XOR operator (^).
•	The result of the XOR operation is a new value.
•	This new value is converted back to a character using the chr () function.
•	The encrypted character is added to the encrypted message.
Decryption:
•	Each character in the encrypted message is XORed with the key using the XOR operator (^).
•	The result of the XOR operation is the original ASCII value of the character.
•	This ASCII value is converted back to a character using the chr () function.
•	The decrypted character is added to the decrypted message.
The original message can be retrieved by XORing the characters using the same key both during encryption and decryption. The XOR operation is reversed and the original values are returned by XORing the characters once more with the same key.

