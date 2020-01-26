# -*- coding: utf-8 -*-
"""
时间: 2019/12/5 17:30

作者: nola2

更改记录:

重要说明: 画线
"""

import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

# 参数一：img绘制的图像；参数二三：线条的起点和终点；参数四：线条颜色蓝色；参数五：线条粗细5px
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
win_name = "line"
cv2.namedWindow(win_name)
cv2.imshow(win_name, img)
cv2.waitKey(0)
cv2.destroyWindow(win_name)
