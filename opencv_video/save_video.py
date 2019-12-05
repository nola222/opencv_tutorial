# -*- coding: utf-8 -*-
"""
时间: 2019/12/5 16:22

作者: nola2

更改记录:

重要说明: 摄像头捕获的视频，沿垂直方向旋转每一帧并保存
"""

import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # FOURCC一个4字节码，确认视频编码格式
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)  # 1水平翻转
        out.write(frame)  # 写入帧

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
