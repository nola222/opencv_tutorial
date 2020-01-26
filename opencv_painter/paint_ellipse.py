# -*- coding: utf-8 -*-
"""
时间: 2020/1/26 10:59

作者: lixianchun@cyai.com

更改记录:

重要说明: 画椭圆
"""

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # 创建一个黑色的image
# 参数一：img表示要绘制图形的image，参数二：表示中心点坐标，参数三：表示长轴与短轴的长度，参数四五六：表示椭圆旋转角度，起始角度，结束角度
# 180半椭圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
win_name = "ellipse"
cv2.namedWindow(win_name)
cv2.imshow(win_name, img)
cv2.waitKey(0)  # 监听键盘事件，0无限期等待
cv2.destroyWindow(win_name)  # 删除创建的窗口
