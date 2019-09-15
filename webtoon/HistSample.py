import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\python_data\\webtoon\\imgs\\43.jpg', cv2.IMREAD_COLOR)

img_b, img_g, img_r = cv2.split(img)
hist_b, bins_b= np.histogram(img_b, 128, [0, 256])
hist_g, bins_g= np.histogram(img_g, 128, [0, 256])
hist_r, bins_r= np.histogram(img_r, 128, [0, 256])
bins_b=bins_b[:-1]
bins_g=bins_g[:-1]
bins_r=bins_r[:-1]
plt.plot(bins_r, hist_r, color=[1,0,0])
plt.show()
plt.plot(bins_g, hist_g, color=[0,1,0])
plt.show()
plt.plot(bins_b, hist_b, color=[0,0,1])

plt.show()
