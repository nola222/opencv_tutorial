# -*- coding: utf-8 -*-
"""
时间: 2020/1/26 10:59

作者: lixianchun@cyai.com

更改记录:

重要说明: 画多边形
"""

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # 创建一个黑色的image
pst = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)  # 指定每个顶点的坐标
pst = pst.reshape((-1, 1, 2))  # 参数一：-1表示这一维度的长度是根据后面的维度计算出来的
cv2.polylines(img, [pst], True, (255, 255, 0))  # 参数二为array；若第三个参数为False，得到的多边形不闭合；参数四天蓝色
win_name = "polygon"
cv2.namedWindow(win_name)
cv2.imshow(win_name, img)
cv2.waitKey(0)  # 监听键盘事件，0无限期等待
cv2.destroyWindow(win_name)  # 删除创建的窗口
