import numpy as np
import matplotlib.pyplot as plt
from skimage import data

img = data.camera()

# Slide 24: row first, then column -> img[row, col], indexing starts at 0
print("shape:", img.shape)
print("img[100, 200] =", img[100, 200])

# Slide 25: slicing
top_left = img[:256, :256]   # first 256 rows, first 256 columns
subsampled = img[::8, ::8]   # every 8th row and column
print("top_left:", top_left.shape)
print("subsampled:", subsampled.shape)

# Slide 26: a slice is a "view", not a copy
a = data.camera()
b = a[:100, :100]            # view
b[:] = 255                   # paint b white
print("view: a[0, 0] =", a[0, 0])

c = data.camera()
d = c[:100, :100].copy()     # real copy
d[:] = 255
print("copy: c[0, 0] =", c[0, 0])

# Slide 27: the uint8 trap
x = np.array([200], dtype=np.uint8)
y = np.array([100], dtype=np.uint8)
print("200 + 100 with uint8 =", x + y)
print("200 + 100 with int16 =", x.astype(np.int16) + y.astype(np.int16))

# Show the slices
plt.subplot(1, 3, 1)
plt.imshow(img, cmap="gray")
plt.title("img")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(top_left, cmap="gray")
plt.title("img[:256, :256]")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(subsampled, cmap="gray")
plt.title("img[::8, ::8]")
plt.axis("off")

plt.show()
