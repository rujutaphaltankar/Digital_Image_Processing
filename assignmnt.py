# Reading and Displaying an Image
import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\Student\Desktop\sunflower.jpg")

if image is None:
    print("Error: Image could not be loaded.")
else:
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.show()