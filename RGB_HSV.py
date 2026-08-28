import cv2
import matplotlib.pyplot as plt

# Take image path from user
image_path = input(r"C:\Users\Rujuta\Documents\3rd Year\Sem 5\DIP\nature.jpg")

# Read the image
image = cv2.imread(image_path)

# Check if image is loaded
if image is None:
    print("Image not found!")
else:
    # Convert BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert RGB image to Grayscale
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

    # Convert RGB image to HSV
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    # Display images
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(rgb_image)
    plt.title("RGB Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(hsv_image)
    plt.title("HSV Image")
    plt.axis("off")

    plt.show()