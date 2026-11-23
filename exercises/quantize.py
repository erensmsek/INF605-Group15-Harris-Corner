import cv2
from skimage import data
import matplotlib.pyplot as plt

img = data.camera()

q16 = (img // 16) * 16
q8 = (img // 32) * 32
q4 = (img // 64) * 64

cv2.imwrite("cameraman_16.png", q16)
cv2.imwrite("cameraman_8.png", q8)
cv2.imwrite("cameraman_4.png", q4)

images = [img, q16, q8, q4]
titles = ["256 levels", "16 levels", "8 levels", "4 levels"]

for i in range(4):
    plt.subplot(1, 4, i + 1)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255)
    plt.title(titles[i])
    plt.axis("off")

plt.show()
