#Neighborhood operations involve examining the pixels around a given pixel. This is common in many image processing tasks such as filtering.
import numpy as np

image = np.array([[10, 20, 30, 40, 50],
                  [15, 25, 35, 45, 55],
                  [20, 30, 40, 50, 60],
                  [25, 35, 45, 55, 65],
                  [30, 40, 50, 60, 70]])

print("Image Matrix:\n")
print(image)

# Select the center pixel
x, y = 2, 2

print("\nSelected Pixel:")
print(f"Position = ({x}, {y})")
print(f"Value = {image[x, y]}")

# 4-Neighborhood
N4 = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

# Diagonal Neighborhood
ND = [(x-1, y-1), (x-1, y+1),
      (x+1, y-1), (x+1, y+1)]

# 8-Neighborhood
N8 = N4 + ND

print("\n4-Neighbors:")
for i, j in N4:
    print(f"({i}, {j}) = {image[i, j]}")

print("\nDiagonal Neighbors:")
for i, j in ND:
    print(f"({i}, {j}) = {image[i, j]}")

print("\n8-Neighbors:")
for i, j in N8:
    print(f"({i}, {j}) = {image[i, j]}")