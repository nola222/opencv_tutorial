# -*- coding: utf-8 -*-
"""
时间: 2019/11/29 16:59

作者: nola2

更改记录:

重要说明:
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('proxy.png', 1)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
