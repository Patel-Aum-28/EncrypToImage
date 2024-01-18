# Image Encryption and Decryption Tool
This project is a simple image encryption and decryption tool developed as part of the internship program at SlashMark, assigned as Task-3.

## Features
- Encryption of image files
- Decryption of encrypted image files
- Secure key generation
- Support for AES encryption algorithm
- Command-line interface

## Requirements
- Python 3.x
- pycryptodome library (install using `pip install pycryptodome`)

## Usage
1. **Encrypt Image:**
    - Run the script and choose the option to encrypt an image.
    - Enter the path of the image file to be encrypted.

2. **Decrypt Image:**
    - Choose the option to decrypt an image.
    - Enter the path of the encrypted image file.
    - Note that for decryption you need `key.pickle` file, which was generated during encryption process.

3. **Exit:**
    - Choose the exit option to terminate the program.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/image-encryption-tool.git
    cd EncrypToImage
    ```

2. Install dependencies:
    ```bash
    pip install pycryptodome
    ```

## Usage Example
```bash
python main.py
```
