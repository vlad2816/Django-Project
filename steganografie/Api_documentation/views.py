from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'Api_documentation/home.html')


def criptare(request):

    import cv2

def encrypt_message_in_photo(photo_path, message):
    # Read the photo
    photo = cv2.imread(photo_path)

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Ensure that the message can fit in the photo
    if len(binary_message) > photo.size:
        raise ValueError("The message is too large to fit in the photo.")

    # Iterate over each pixel in the photo
    for i, bit in enumerate(binary_message):
        # Get the pixel coordinates
        x = i % photo.shape[1]
        y = i // photo.shape[1]

        # Modify the least significant bit of the pixel's RGB values
        pixel = photo[y, x]
        pixel[0] = (pixel[0] & 0xFE) | int(bit)  # Blue channel
        pixel[1] = (pixel[1] & 0xFE) | int(bit)  # Green channel
        pixel[2] = (pixel[2] & 0xFE) | int(bit)  # Red channel

    # Save the modified photo
    encrypted_photo_path = "encrypted_photo.jpg"
    cv2.imwrite(encrypted_photo_path, photo)
    print(f"Encrypted photo saved as: {encrypted_photo_path}")

# Example usage
photo_path = "photo.jpg"
message = "This is a secret message!"

encrypt_message_in_photo(photo_path, message)

    return render(request, 'Api_documentation/criptare.html')
