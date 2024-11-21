Image Encryption and Decryption Tool

This project is a simple **Image Encryption and Decryption Tool** that manipulates the RGB pixel values of an image to provide basic encryption. The tool swaps the Red (R) and Blue (B) channels of each pixel for encryption and reverses the process for decryption.

---

Features

- Encrypt Images: Swaps the Red (R) and Blue (B) channels of each pixel.
- Decrypt Images: Reverses the swapping to restore the original image.
- Interactive Menu: Allows users to choose between encrypting, decrypting, or exiting the tool.
- Dynamic Input/Output Paths: Users can specify custom file paths for input and output images.

---

Prerequisites

Ensure you have Python installed along with the required library:

```bash
pip install pillow
```

---

How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/image-encryption-tool.git
   cd image-encryption-tool
   ```

2. Run the tool:
   ```bash
   python image_encryption.py
   ```

3. Follow the interactive prompts:
   - Encrypt an Image: Provide the path of the image to encrypt and the path to save the encrypted image.
   - Decrypt an Image: Provide the path of the encrypted image and the path to save the decrypted image.

---

Example Usage

Encryption:
```plaintext
Welcome to the Image Encryption/Decryption Tool!

Menu:
1. Encrypt an image
2. Decrypt an image
3. Exit
Enter your choice (1/2/3): 1
Enter the path of the image to encrypt: input.jpg
Enter the path to save the encrypted image: encrypted_image.jpg
Image encrypted successfully and saved to encrypted_image.jpg!
```

Decryption:
```plaintext
Menu:
1. Encrypt an image
2. Decrypt an image
3. Exit
Enter your choice (1/2/3): 2
Enter the path of the encrypted image to decrypt: encrypted_image.jpg
Enter the path to save the decrypted image: decrypted_image.jpg
Image decrypted successfully and saved to decrypted_image.jpg!
```

---

File Structure

```plaintext
.
├── image_encryption.py    # Main script for image encryption and decryption
├── README.md              # Documentation
```

---

Notes

1. Supported Image Formats: Common formats such as `.jpg`, `.png`, `.bmp` are supported.
2. Input and Output: Ensure the input image exists, and you have write permissions for the output path.
3. Image Distortion: Using this tool with an encrypted image and not swapping back the channels can distort the image.

---

Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements or suggestions.

---

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
