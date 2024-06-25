import pyautogui
import time
import pyperclip

import pytesseract
from PIL import ImageGrab
#打开浏览器
pyautogui.click(x=171, y=1062)
time.sleep(3)
#找到对应页签
pyautogui.click(x=313, y=58)
chinese_text = 'https://www.126.com/'
pyperclip.copy(chinese_text)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)
#输入账号
pyautogui.doubleClick(x=1214, y=471)
pyautogui.hotkey('Backspace')
chinese_text = 'crsun49'
pyperclip.copy(chinese_text)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
#输入密码
pyautogui.click(x=1214, y=537)
chinese_text = '1234567'
pyperclip.copy(chinese_text)
pyautogui.hotkey('ctrl', 'v')
# 将中文字符复制到剪贴板
time.sleep(1)

pyautogui.press('enter')



# 截取屏幕指定区域的截图
left = 0
top = 0
width = 313
height = 58
screenshot = ImageGrab.grab(bbox=(left, top, left+width, top+height))

# 将截图转换为灰度图像
gray_image = screenshot.convert('L')

# 使用Tesseract进行OCR识别
text = pytesseract.image_to_string(gray_image)

print(text)