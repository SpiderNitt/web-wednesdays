import numpy as np
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow
import cv2
import os

img_org = cv2.imread('image/path/here')

img = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)
ishape = img.shape
print(img.shape)
img=cv2.resize(img, (int(ishape[1]/2), int(ishape[0]/2)))
print(img.shape)
ishape = img.shape
plt.figure(figsize=(10,10))
plt.imshow(img, cmap='Greys_r') 

def hist_and_plot(img):
  hist,bins = np.histogram(img.flatten(),256,[0,256])
  cdf = hist.cumsum()
  cdf_normalized = cdf / cdf.max()
  # cdf_normalized = cdf * hist.max()/ cdf.max()
  fig, ax = plt.subplots(2,1)
  ax[0].plot(cdf_normalized, color = 'b')
  ax[1].hist(img.flatten(),256,[0,256], color = 'r')
  plt.xlim([0,256])
  # plt.legend(('cdf','histogram'))
  plt.show()
  return cdf_normalized

X0 = 0
Xl = 255

def histf(x):
  return X0 + (Xl-X0)*cdf_normalized[x]

print(histf(1))

hist_img = np.array(list(map(histf, img.flatten())))
hist,bins = np.histogram(hist_img,256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf / cdf.max()
fig, ax = plt.subplots(2,1)
ax[0].plot(cdf_normalized, color = 'b')
print(hist.shape)
ax[1].bar(np.arange(hist.shape[0]), hist, color = 'r')
plt.xlim([0,256])
# plt.legend(('cdf','histogram'))

plt.figure(figsize=(10, 10))
img_ret_he = hist_img.reshape(ishape)
plt.imshow(img_ret_he, cmap='Greys_r')