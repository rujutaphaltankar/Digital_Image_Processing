from PIL import Image
import matplotlib.pyplot as plt

# Function to Display Image
def show_image(image, title):
    plt.figure(figsize=(6, 5))
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()


# Resize Image
def resize_image(input_path, output_path, size):
    image = Image.open(input_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)

    print("Image Resized and Saved to:", output_path)
    show_image(resized_image, "Resized Image")


# Crop Image
def crop_image(input_path, output_path, crop_box):
    image = Image.open(input_path)
    cropped_image = image.crop(crop_box)
    cropped_image.save(output_path)

    print("Image Cropped and Saved to:", output_path)
    show_image(cropped_image, "Cropped Image")


# Flip Image
def flip_image(input_path, output_path, direction):
    image = Image.open(input_path)

    if direction == "horizontal":
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction == "vertical":
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        print("Error! Direction should be 'horizontal' or 'vertical'")
        return

    flipped_image.save(output_path)

    print("Image Flipped and Saved to:", output_path)
    show_image(flipped_image, "Flipped Image")


# Rotate Image
def rotate_image(input_path, output_path, angle):
    image = Image.open(input_path)
    rotated_image = image.rotate(angle, expand=True)
    rotated_image.save(output_path)

    print("Image Rotated and Saved to:", output_path)
    show_image(rotated_image, "Rotated Image")


# Main Program
input_file = r"C:\Users\Rujuta\Downloads\nature.jpg"

# Show Original Image
original = Image.open(input_file)
show_image(original, "Original Image")

# Resize
resize_image(input_file, r"C:\Users\Rujuta\Downloads\resized.jpg", (800, 600))

# Crop
crop_image(input_file, r"C:\Users\Rujuta\Downloads\cropped.jpg", (150, 150, 300, 500))

# Flip
flip_image(input_file, r"C:\Users\Rujuta\Downloads\flipped.jpg", "horizontal")

# Rotate
rotate_image(input_file, r"C:\Users\Rujuta\Downloads\rotated.jpg", 270)








