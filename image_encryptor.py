from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            # Simple encryption by shifting RGB values using key
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            # Reverse the encryption by subtracting the key
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    print("=== Image Encryption Tool ===")
    choice = input("Type 'encrypt' or 'decrypt': ").lower()
    input_path = input("Enter the path of the image file (e.g., image.jpg): ")
    output_path = input("Enter the name for the output file (e.g., encrypted.jpg): ")
    
    try:
        key = int(input("Enter a numeric key (1-255): "))
        if not (1 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Invalid key. Please enter a number between 1 and 255.")
        return

    if not os.path.exists(input_path):
        print("Image file not found.")
        return

    if choice == 'encrypt':
        encrypt_image(input_path, output_path, key)
    elif choice == 'decrypt':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid option. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
