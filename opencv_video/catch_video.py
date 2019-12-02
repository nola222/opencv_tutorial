# -*- coding: utf-8 -*-
"""
时间: 2019/11/29 17:08

作者: nola2

更改记录:

重要说明: 使用摄像头捕获一段视频灰度显示
"""

import cv2

# 实例化 参数为设备索引号即指定摄像头，一般电脑内置摄像头参数为0，也可设置1或其他摄像头选择别的摄像头
cap = cv2.VideoCapture(0)
# 初始化不成功会抛异常，cap.isOpened()检查是否开启，若没有开启使用cap.open()开启
# cap.get(propId) propId：0~18 代表视频属性。如3，4读取每一帧的宽高。使用ret=cap.set(3, 320)设置宽高

while True:
    # 一帧帧捕获
    ret, frame = cap.read()  # 返回值ret bool帧读取是否正确
    # 设置视频灰度
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 显示帧
    cv2.imshow('frame', gray)
    k = cv2.waitKey(1)  # 无输入时为-1
    print(k)
    if k & 0xFF == ord('q'):  # 113
        break

cap.release()  # 停止捕获视频
cv2.destroyAllWindows()
