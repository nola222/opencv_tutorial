# -*- coding: utf-8 -*-
"""
时间: 2019/11/29 16:02

作者: nola2

更改记录:

重要说明: 窗口大小可更改
"""

import cv2

# load an image in origin scale
img = cv2.imread('proxy.png', 1)  # 路径错的OpenCV不会报错，print img时得到结果为None
# 创建窗口设置可以调整大小 --> WINDOW_NORMAL，初始大小使用的是WINDOW_AUTOSIZE
cv2.namedWindow('widget_name', cv2.WINDOW_NORMAL)
# show an image
cv2.imshow('widget_name', img)  # 参数一窗口名称，窗口会自动调整为图像大小，可创建多个窗口
# 键盘事件，参数为键盘事件等待时间毫秒数，0将无限期的等待键盘输入；特定毫秒内，键入任何键，函数返回键的ASCII码值，若无键入到时返回-1。
# 也可用于监听检测某个键
cv2.waitKey(0)
cv2.destroyAllWindows()  # 删除所有创建的窗口


