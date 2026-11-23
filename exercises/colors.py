import cv2
import matplotlib.pyplot as plt
from skimage import data

# Show a grayscale image with OpenCV (slide 20)
img = data.camera()
cv2.imshow("cameraman", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Color image (slide 22)
rgb = data.astronaut()
bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)   # convert to OpenCV channel order

wrong = bgr                                    # showing BGR directly gives wrong colors
correct = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB) # conversion from the slide

plt.subplot(1, 2, 1)
plt.imshow(wrong)
plt.title("BGR (wrong colors)")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(correct)
plt.title("Converted to RGB")
plt.axis("off")

plt.show()
