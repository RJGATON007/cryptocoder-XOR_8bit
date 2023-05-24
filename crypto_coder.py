# the key is masked with 0xFF (which represents 8 bits with all bits set to 1)
# during the XOR operation. This ensures that only the lower 8 bits of the
# key are used for encryption and decryption, effectively limiting it to 8-bit values.

from colorama import Fore


def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        encrypted_char = chr(ord(char) ^ (key & 0xFF))  # mask
        encrypted_message += encrypted_char
    return encrypted_message


def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        decrypted_char = chr(ord(char) ^ (key & 0xFF))
        decrypted_message += decrypted_char
    return decrypted_message


# Encrypt a message and save it to encrypted.txt
def encrypt_file(file_path, key):
    with open(file_path, 'r') as file:
        plaintext = file.read()
        encrypted_message = encrypt(plaintext, key)
        with open('encrypted.txt', 'w') as encrypted_file:
            encrypted_file.write(encrypted_message)


# Decrypt a message and save it to decrypted.txt
def decrypt_file(file_path, key):
    with open(file_path, 'r') as file:
        encrypted_message = file.read()
        decrypted_message = decrypt(encrypted_message, key)
        with open('decrypted.txt', 'w') as decrypted_file:
            decrypted_file.write(decrypted_message)


# Example usage of key (8-bit)
plaintext_file = 'plaintext.txt'
# SET KEY FROM 0-255
# FOR EXAMPLE: 1, 3, 5, 7, 9, 103, 127, 254
encryption_key = 3

encrypt_file(plaintext_file, encryption_key)
print(Fore.YELLOW + "Encryption complete. Encrypted message saved to 'encrypted.txt'.")
encrypted_file = 'encrypted.txt'

decrypt_file(encrypted_file, encryption_key)
print(Fore.BLUE + "Decryption complete. Decrypted message saved to 'decrypted.txt'.")

decrypted_file = 'decrypted.txt'
