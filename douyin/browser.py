import pyautogui
import time
import pyperclip
#打开浏览器
pyautogui.click(x=171, y=1062)
time.sleep(3)
#找到对应页签
pyautogui.click(x=313, y=58)
chinese_text = 'https://c2.binjie.fun/'
pyperclip.copy(chinese_text)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=514, y=991)
# 将中文字符复制到剪贴板
chinese_text = '你能告诉我python怎么获取浏览器上的文本'
pyperclip.copy(chinese_text)
pyautogui.hotkey('ctrl', 'v')
#pyautogui.press('enter')