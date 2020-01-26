# -*- coding: utf-8 -*-
"""
时间: 2020/1/26 10:59

作者: lixianchun@cyai.com

更改记录:

重要说明: 画圆
"""

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # 创建一个黑色的image
# 参数一：img表示要绘制图形的image，参数二：表示圆心，参数三：表示半径，参数五：表示线条的粗细3px
cv2.circle(img, (447, 63), 63, (0, 255, 0), 3)
win_name = "circle"
cv2.namedWindow(win_name)
cv2.imshow(win_name, img)
cv2.waitKey(0)  # 监听键盘事件，0无限期等待
cv2.destroyWindow(win_name)  # 删除创建的窗口
