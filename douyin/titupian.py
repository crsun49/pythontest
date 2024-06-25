# 导入依赖库
import cv2
import pytesseract

# 读取图片
img = cv2.imread('C:/jjj55555.png')

# 配置pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 识别图片中的文字
text = pytesseract.image_to_string(img, lang='chi_sim')

# 输出识别结果
print(text)
