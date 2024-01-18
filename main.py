from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
import sys
import base64
import pickle

def generate_key():
    return get_random_bytes(32)

def encrypt_image(image_path, key):
    key_str = key.hex()

    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    with open(image_path, 'rb') as file:
        data = file.read()

    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    encrypted_data_str = base64.b64encode(iv + encrypted_data).decode()

    with open(image_path + '.enc', 'w') as file:
        file.write(encrypted_data_str)

    os.remove(image_path)

    with open('key.pickle', 'wb') as file:
        pickle.dump(key, file)
    
    temp = str(image_path)
    name = temp + ".enc" 

    print(f'Image encrypted successfully, and stored as {name}!')

def decrypt_image(encrypted_image_path):
    if not os.path.exists('key.pickle'):
        print("Error: Key file not found. Please encrypt an image first.")
        return

    with open('key.pickle', 'rb') as file:
        key = pickle.load(file)

    key_str = key.hex()

    try:
        with open(encrypted_image_path, 'r') as file:
            encrypted_data_str = file.read()

        encrypted_data = base64.b64decode(encrypted_data_str)
        iv = encrypted_data[:AES.block_size]
        encrypted_data = encrypted_data[AES.block_size:]

        cipher = AES.new(key, AES.MODE_CBC, iv)

        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        with open(os.path.splitext(encrypted_image_path)[0], 'wb') as file:
            file.write(decrypted_data)

        os.remove(encrypted_image_path)
        temp = str(encrypted_image_path)
        name = temp[:-4]
        print(f'Image decrypted successfully, and stored as {name}!')

    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print('\n1. Encrypt image\n2. Decrypt image\n3. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            image_path = input('Enter the name of image file (With Path): ')
            encrypt_image(image_path, generate_key())

        elif choice == '2':
            encrypted_image_path = input('Enter the name of encrypted image file (With Path): ')
            decrypt_image(encrypted_image_path)

        elif choice == '3':
            sys.exit(0)

        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
