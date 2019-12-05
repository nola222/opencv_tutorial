# -*- coding: utf-8 -*-
"""
时间: 2019/12/2 10:59

作者: nola2

更改记录:

重要说明: 与从摄像头捕获一样，将设备索引号改成视频文件的名字。
"""

import cv2

# 初始化
cap = cv2.VideoCapture(0)  # 参数0 一般电脑内置摄像头参数

# 定义4字符编码表示视频数据流格式，即输入4字符代码即可得到对应的视频编码器。
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 使用XVID视频编码器
# 创建VideoWriter对象 参数三帧率
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 0)  # 0垂直翻转，1水平翻转，-1水平垂直翻转
        # 保存视频
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
