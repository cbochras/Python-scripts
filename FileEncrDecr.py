""" The code takes user input to either encrypt or decrypt a file. If the user chooses to encrypt a file,
 the code prompts the user to enter the path of the file to be encrypted and an encryption key. 
The file is then encrypted using the Advanced Encryption Standard (AES) in cipher block chaining (CBC) mode, 
and the encrypted file is saved to a subdirectory called "encrypted" in the same directory as the input file. 
If the user chooses to decrypt a file, the code prompts the user to enter the path of the encrypted file and the decryption key. 
The file is then decrypted and saved to a subdirectory called "decrypted" in the same directory as the encrypted file.
The code uses the pycrypto library to perform the encryption and decryption, and checks whether the output directory exists and prompts 
the user to overwrite or choose a different file name if a file with the same name already exists."""

import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_file(key, input_file_path):
    # Check if output directory exists, create it if not
    output_dir = os.path.join(os.path.dirname(input_file_path), "encrypted")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get output file path
    output_file_name = "encrypted_" + os.path.basename(input_file_path)
    output_file_path = os.path.join(output_dir, output_file_name)

    # Check if output file already exists, prompt user to overwrite or choose a different name
    while os.path.exists(output_file_path):
        response = input(f"The file '{output_file_name}' already exists. Do you want to overwrite it? (y/n) ")
        if response.lower() == "y":
            break
        else:
            output_file_name = input("Please enter a different name for the output file: ")
            output_file_path = os.path.join(output_dir, output_file_name)

    # Generate random IV
    iv = get_random_bytes(16)

    # Encrypt file
    chunk_size = 64 * 1024
    filesize = str(os.path.getsize(input_file_path)).zfill(16).encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(input_file_path, 'rb') as infile, open(output_file_path, 'wb') as outfile:
        outfile.write(filesize)
        outfile.write(iv)
        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += b' ' * (16 - len(chunk) % 16)
            outfile.write(cipher.encrypt(chunk))

    return output_file_path


def decrypt_file(key, input_file_path):
    # Check if output directory exists, create it if not
    output_dir = os.path.join(os.path.dirname(input_file_path), "decrypted")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get output file path
    output_file_name = "decrypted_" + os.path.basename(input_file_path)[10:]
    output_file_path = os.path.join(output_dir, output_file_name)

    # Check if output file already exists, prompt user to overwrite or choose a different name
    while os.path.exists(output_file_path):
        response = input(f"The file '{output_file_name}' already exists. Do you want to overwrite it? (y/n) ")
        if response.lower() == "y":
            break
        else:
            output_file_name = input("Please enter a different name for the output file: ")
            output_file_path = os.path.join(output_dir, output_file_name)

    # Decrypt file
    chunk_size = 64 * 1024
    with open(input_file_path, 'rb') as infile, open(output_file_path, 'wb') as outfile:
        filesize = int(infile.read(16))
        iv = infile.read(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            outfile.write(cipher.decrypt(chunk))
        outfile.truncate(filesize)

    return output_file_path
# Get user input
action = input("Do you want to encrypt or decrypt a file? (e/d) ")
while action.lower() not in ['e', 'd']:
    action = input("Invalid input. Please enter 'e' to encrypt or 'd' to decrypt a file: ")

input_file_path = input("Enter the path to the file: ")

if action == "e":
    # Get encryption key from user
    key = input("Enter the encryption key (32 characters): ")
    while len(key) != 32:
        key = input("Invalid key. Please enter a key with 32 characters: ")

    # Encrypt file and get output file path
    output_file_path = encrypt_file(key.encode(), input_file_path)

    print(f"File encrypted successfully. Output file: {output_file_path}")

elif action == "d":
    # Get decryption key from user
    key = input("Enter the decryption key (32 characters): ")
    while len(key) != 32:
        key = input("Invalid key. Please enter a key with 32 characters: ")

    # Decrypt file and get output file path
    output_file_path = decrypt_file(key.encode(), input_file_path)

    print(f"File decrypted successfully. Output file: {output_file_path}")
