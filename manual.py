import cv2
import numpy as np

img = cv2.imread("data/scene.png")

if img is None:
    raise ValueError("Image not found")

message = "Hi! This is a ###message###"
binary_msg = "".join(format(ord(i), "08b") for i in message)

idx = 0
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(3):
            if idx < len(binary_msg):
                img[i][j][k] = np.uint8((img[i][j][k] & 254) | int(binary_msg[idx]))
                idx += 1

cv2.imwrite("data/compromised_manual.png", img)
