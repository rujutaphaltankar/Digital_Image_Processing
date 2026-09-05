import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import sqrt, atan2, pi

# Read Image and convert it into grayscale
img = Image.open(r"C:\Users\Student\Desktop\monkey.jpg")
img = img.convert("L")
img = np.array(img, dtype=np.float32)

# Gaussian Blur (3×3 Kernel)-
gaussian = np.array([[1,2,1],
                     [2,4,2],
                     [1,2,1]], dtype=float)

gaussian = gaussian / gaussian.sum()

rows, cols = img.shape
blur = np.zeros_like(img)

for i in range(1, rows-1):
    for j in range(1, cols-1):
        blur[i,j] = np.sum(img[i-1:i+2, j-1:j+2] * gaussian)

# Sobel Gradient
Gx = np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])

Gy = np.array([[1,2,1],
               [0,0,0],
               [-1,-2,-1]])

Ix = np.zeros_like(blur)
Iy = np.zeros_like(blur)

for i in range(1, rows-1):
    for j in range(1, cols-1):
        region = blur[i-1:i+2, j-1:j+2]
        Ix[i,j] = np.sum(region * Gx)
        Iy[i,j] = np.sum(region * Gy)

gradient = np.sqrt(Ix**2 + Iy**2)
gradient = gradient / gradient.max() * 255

angle = np.arctan2(Iy, Ix) * 180 / np.pi
angle[angle < 0] += 180

# Non-Maximum Suppression
nms = np.zeros_like(gradient)

for i in range(1, rows-1):
    for j in range(1, cols-1):

        q = 255
        r = 255

        if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
            q = gradient[i,j+1]
            r = gradient[i,j-1]

        elif (22.5 <= angle[i,j] < 67.5):
            q = gradient[i+1,j-1]
            r = gradient[i-1,j+1]

        elif (67.5 <= angle[i,j] < 112.5):
            q = gradient[i+1,j]
            r = gradient[i-1,j]

        elif (112.5 <= angle[i,j] < 157.5):
            q = gradient[i-1,j-1]
            r = gradient[i+1,j+1]

        if gradient[i,j] >= q and gradient[i,j] >= r:
            nms[i,j] = gradient[i,j]
        else:
            nms[i,j] = 0

# Double Threshold
high = 80
low = 30

strong = 255
weak = 75

edges = np.zeros_like(nms)

strong_i, strong_j = np.where(nms >= high)
weak_i, weak_j = np.where((nms >= low) & (nms < high))

edges[strong_i, strong_j] = strong
edges[weak_i, weak_j] = weak

# Hysteresis
for i in range(1, rows-1):
    for j in range(1, cols-1):

        if edges[i,j] == weak:

            if ((edges[i+1,j] == strong) or
                (edges[i-1,j] == strong) or
                (edges[i,j+1] == strong) or
                (edges[i,j-1] == strong) or
                (edges[i-1,j-1] == strong) or
                (edges[i-1,j+1] == strong) or
                (edges[i+1,j-1] == strong) or
                (edges[i+1,j+1] == strong)):

                edges[i,j] = strong

            else:
                edges[i,j] = 0

# Displaying Final Results
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(gradient, cmap='gray')
plt.title("Gradient")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(edges, cmap='gray')
plt.title("Canny Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()