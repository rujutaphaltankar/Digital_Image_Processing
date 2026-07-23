import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# Convert to grayscale
img = Image.open("sunflower.jpg").convert("L")  
img = np.array(img)

def sampling(image, factor):
    """
    Reduce image resolution by selecting every 'factor' pixel.
    """
    sampled = image[::factor, ::factor]
    return sampled

# Image Quantization Function
def quantization(image, bits):
    """
    Reduce the number of gray levels.
    """
    levels = 2 ** bits
    step = 256 / levels

    quantized = np.floor(image / step) * step
    quantized = quantized.astype(np.uint8)

    return quantized

# Perform Sampling

sample2 = sampling(img,2)
sample4 = sampling(img,4)


# Perform Quantization
quant8 = quantization(img,8)
quant4 = quantization(img,4)
quant2 = quantization(img,2)

# Display Results

plt.figure(figsize=(14,8))

plt.subplot(2,3,1)
plt.imshow(img,cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(sample2,cmap='gray')
plt.title("Sampling Factor = 2")
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(sample4,cmap='gray')
plt.title("Sampling Factor = 4")
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(quant8,cmap='gray')
plt.title("8-bit Quantization")
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(quant4,cmap='gray')
plt.title("4-bit Quantization")
plt.axis('off')

plt.subplot(2,3,6)
plt.imshow(quant2,cmap='gray')
plt.title("2-bit Quantization")
plt.axis('off')

plt.tight_layout()
plt.show()