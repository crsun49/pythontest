
import pyautogui
import time
import pytesseract
from PIL import ImageGrab
import cv2
#打开浏览器
pyautogui.click(x=171, y=1062)
time.sleep(3)

# 截取屏幕指定区域的截图
left = 280
top = 355
width = 1037
height = 314

screenshot = ImageGrab.grab(bbox=(left, top, left+width, top+height))
gray_image = screenshot.convert('L')


#img = pyautogui.screenshot(region=[left, top, width, height])
#img.convert('L').save(r'C:\img.jpg')


# 保存截图到本地
gray_image.save('C:\screensho45.png')
time.sleep(3)
# 将截图转换为灰度图像
#screenshot.convert('L').save('C:\screenshot.png')

# 配置中文语言包文件路径（根据实际文件路径进行设置）
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#tessdata_dir_config = '--tessdata-dir "F:/软件工具"'

# 使用Tesseract进行OCR识别
text = pytesseract.image_to_string(gray_image, lang='chi_sim')
#text = pytesseract.image_to_string(gray_image)

print(text)

