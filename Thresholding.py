import numpy as np
 
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = np.zeros((rows, cols), dtype=int)

print("Enter matrix elements (0-255):")

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = int(input(f"Element [{i}][{j}]: "))

print("\nOriginal Matrix:")
print(matrix)


T = int(input("\nEnter manual threshold T: "))

manual = np.where(matrix > T, 255, 0)

print("\n--- MANUAL THRESHOLDING ---")
print("Threshold =", T)
print(manual)


pixels = matrix.flatten()

best_T = 0
max_variance = -1

for T in range(256):

    class1 = pixels[pixels <= T]
    class2 = pixels[pixels > T]

    if len(class1) == 0 or len(class2) == 0:
        continue

    w1 = len(class1) / len(pixels)
    w2 = len(class2) / len(pixels)

    mean1 = np.mean(class1)
    mean2 = np.mean(class2)

    # Between-class variance
    variance = w1 * w2 * (mean1 - mean2) ** 2

    if variance > max_variance:
        max_variance = variance
        best_T = T

otsu = np.where(matrix > best_T, 255, 0)

print("\n--- OTSU'S THRESHOLDING ---")
print("Optimal Threshold =", best_T)
print(otsu)


pixels = matrix.flatten()

# Initial threshold = mean of all pixels
T = np.mean(pixels)

while True:

    # Divide pixels into two groups
    group1 = pixels[pixels <= T]
    group2 = pixels[pixels > T]

    # Calculate means
    mean1 = np.mean(group1)
    mean2 = np.mean(group2)

    # New threshold
    new_T = (mean1 + mean2) / 2

    # Stop when threshold does not change
    if abs(new_T - T) < 0.01:
        break

    T = new_T

iterative_T = round(new_T)

iterative = np.where(matrix > iterative_T, 255, 0)

print("\n--- ITERATIVE THRESHOLDING ---")
print("Optimal Threshold =", iterative_T)
print(iterative)
