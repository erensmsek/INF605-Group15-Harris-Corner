import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

img = data.camera()

# Interpolation: downscale, then upscale again
small = cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)
big = cv2.resize(small, (512, 512), interpolation=cv2.INTER_CUBIC)
print("small:", small.shape, "big:", big.shape)

# Connected components: first convert the image to black and white
binary = (img > 128).astype(np.uint8)
n, labels = cv2.connectedComponents(binary, connectivity=8)
print("number of connected components (including background):", n)

# Slide 21: wrong file path
wrong = cv2.imread("missing_file.png", cv2.IMREAD_GRAYSCALE)
print("imread result for a wrong path:", wrong)

plt.subplot(1, 4, 1)
plt.imshow(img, cmap="gray")
plt.title("original")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(small, cmap="gray")
plt.title("64x64")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(big, cmap="gray")
plt.title("back to 512x512")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(labels, cmap="nipy_spectral")
plt.title("components")
plt.axis("off")

plt.show()
