import cv2
from skimage import data
import matplotlib.pyplot as plt

img = data.camera()
print(img.shape, img.dtype)

cv2.imwrite("cameraman.png", img)

img2 = cv2.imread("cameraman.png", cv2.IMREAD_GRAYSCALE)
print("File read successfully?", img2 is not None)

plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()