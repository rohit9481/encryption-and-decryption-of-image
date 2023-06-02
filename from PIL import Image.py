from PIL import Image
from tkinter import Tk, filedialog
#to select an image file from our desktop, you can use the tkinter library in Python(it is used for GUI)
# Encryption function
def encrypt(image_path, key):
    # Open the image
    image = Image.open(image_path)

    # Get the width and height of the image
    width, height = image.size

    # Convert the key to a list of bytes
    key_bytes = bytearray(key, 'utf-8')

    # Create a new image with the same size and mode as the original image
    encrypted_image = Image.new("RGB", (width, height))

    # Loop through each pixel of the image
    for y in range(height):
        for x in range(width):
            # Get the pixel value at the current position
            pixel = image.getpixel((x, y))

            # Get the corresponding byte from the key
            key_byte = key_bytes[(y * width + x) % len(key_bytes)]

            # Perform XOR operation between the pixel value and the key byte
            encrypted_pixel = tuple(p ^ key_byte for p in pixel)

            # Set the encrypted pixel value in the new image
            encrypted_image.putpixel((x, y), encrypted_pixel)

    # Save the encrypted image
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully!")

# Decryption function
def decrypt(encrypted_image_path, key):
    # Open ency
    encrypted_image = Image.open(encrypted_image_path)

    # width and height of the image
    width, height = encrypted_image.size

    # Convert the key to a list of bytes
    key_bytes = bytearray(key, 'utf-8')

    # Create a new image with the same size and mode as the encrypted image
    decrypted_image = Image.new("RGB", (width, height))

    # Loop through each pixel of the encrypted image
    for y in range(height):
        for x in range(width):
            # Get the encrypted pixel value at the current position
            encrypted_pixel = encrypted_image.getpixel((x, y))

            # Get the corresponding byte from the key
            key_byte = key_bytes[(y * width + x) % len(key_bytes)]

            # Perform XOR operation between the encrypted pixel value and the key byte
            decrypted_pixel = tuple(p ^ key_byte for p in encrypted_pixel)

            # Set the decrypted pixel value in the new image
            decrypted_image.putpixel((x, y), decrypted_pixel)

    # Save image
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully!")

# Tkinter root window
root = Tk()
root.withdraw()  # Hiding the root window

# select an image file
image_path = filedialog.askopenfilename(title="Select Image File", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))

# Check if the user selected a file
if image_path:
    key = input("Enter the encryption/decryption key: ")
    encrypt(image_path, key)

    decrypt("encrypted_image.png", key)
else:
    print("No image file selected.")
