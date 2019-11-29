# -*- coding: utf-8 -*-
"""
时间: 2019/11/29 16:26

作者: nola2

更改记录:

重要说明: 键盘事件键入S保存后退出，键入ESC退出不保存
"""

import cv2

img = cv2.imread('proxy.png', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    # wait for 's' key to save and exit
    cv2.imwrite('proxy_keyboard.png', img)
    cv2.destroyAllWindows()
