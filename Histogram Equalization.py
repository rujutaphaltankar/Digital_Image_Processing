# Histogram Equalization (Without Libraries)

# Gray levels (0 to 7)
gray_levels = [0, 1, 2, 3, 4, 5, 6, 7]

# Number of pixels for each gray level
pixels = [9, 8, 11, 4, 10, 15, 4, 3]

# Step 1: Find total number of pixels
total_pixels = sum(pixels)

# Step 2: Calculate PDF
pdf = []
for p in pixels:
    pdf.append(p / total_pixels)

# Step 3: Calculate CDF
cdf = []
running_sum = 0

for value in pdf:
    running_sum += value
    cdf.append(running_sum)

# Step 4: Calculate New Gray Levels
new_levels = []

for value in cdf:
    new_levels.append(round(value * 7))

# Step 5: Calculate New Histogram
new_histogram = [0] * 8

for i in range(len(gray_levels)):
    new_histogram[new_levels[i]] += pixels[i]

# Display Histogram Equalization Table
print("Histogram Equalization Table")
print("-" * 80)

print(f"{'Gray':<10}{'Pixels':<10}{'PDF':<12}{'CDF':<12}{'CDF*7':<12}{'New Level'}")

print("-" * 80)

for i in range(len(gray_levels)):
    print(f"{gray_levels[i]:<10}"
          f"{pixels[i]:<10}"
          f"{pdf[i]:<12.4f}"
          f"{cdf[i]:<12.4f}"
          f"{cdf[i]*7:<12.4f}"
          f"{new_levels[i]}")

# Display New Histogram
print("\nNew Histogram")
print("-" * 30)

print(f"{'Gray Level':<15}{'Pixels'}")

for i in range(8):
    print(f"{i:<15}{new_histogram[i]}")