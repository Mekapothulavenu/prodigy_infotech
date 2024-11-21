from PIL import Image

def encrypt_image(input_path, output_path):
    """
    Encrypts an image by swapping the R and B channels of each pixel.
    """
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Swap R and B channels
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print(f"Image encrypted successfully and saved to {output_path}!")

def decrypt_image(input_path, output_path):
    """
    Decrypts an image by swapping the R and B channels of each pixel back.
    """
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Swap R and B channels back
            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print(f"Image decrypted successfully and saved to {output_path}!")

def main():
    print("Welcome to the Image Encryption/Decryption Tool!")
    while True:
        print("\nMenu:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            input_path = input("Enter the path of the image to encrypt: ").strip()
            output_path = input("Enter the path to save the encrypted image: ").strip()
            encrypt_image(input_path, output_path)

        elif choice == "2":
            input_path = input("Enter the path of the encrypted image to decrypt: ").strip()
            output_path = input("Enter the path to save the decrypted image: ").strip()
            decrypt_image(input_path, output_path)

        elif choice == "3":
            print("Exiting the tool. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
