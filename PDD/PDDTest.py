import uiautomator2 as u2
import time
import random
import os
import pytesseract
from PIL import Image
import io
d = u2.connect_usb('v8eqhujjwwknkjyt')
print(d.info)
#C:\Program Files\Tesseract-OCR
#d.swipe(0.165, 0.619, 0.165, 0.398, duration=0.4)
time.sleep(1)
#d.swipe(0.165, 0.619, 0.165, 0.398, duration=0.3)
d.click(0.471, 0.645)
time.sleep(70)
d.click(0.909, 0.069)
time.sleep(70)
#
# # # 截取屏幕截图
# # screenshot_path = "C:/Users/Administrator/Desktop/33/mk/screenshot.png"
# #
# # d.screenshot(screenshot_path)
# # d.sleep(4)
#
# # 加载截图
# # 指定图片路径
# image_path = r'C:/Users/Administrator/Desktop/33/mk/screenshot.png'
#
# # 打开图片
# image = Image.open(image_path)
#
# # 识别图片中的文字
# text = pytesseract.image_to_string(image)
# # 打印提取的文字
# print("提取的文字：")
# print(text)