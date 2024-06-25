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
#ime.sleep(10)
i=1
for i in range(1,50):
    d.swipe(0.165, 0.619, 0.165, 0.398, duration=0.4)
    number = random.uniform(1, 2)
    time.sleep(number)
    d.swipe(0.165, 0.619, 0.165, 0.398, duration=0.3)
    time.sleep(number)
    d.click(0.471, 0.645)
    time.sleep(70)
    d.click(0.909, 0.069)
    time.sleep(10)