# -*- coding: utf-8 -*-
"""
时间: 2020/1/26 10:59

作者: lixianchun@cyai.com

更改记录:

重要说明: 画矩形
"""

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)  # 绿色矩形
win_name = "rectangle"
cv2.namedWindow(win_name)
cv2.imshow(win_name, img)
cv2.waitKey(0)  # 监听键盘事件，0无限期等待
cv2.destroyWindow(win_name)  # 删除创建的窗口
