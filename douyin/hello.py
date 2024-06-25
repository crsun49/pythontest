import pyautogui
import time
import pyperclip

# 将中文字符复制到剪贴板
chinese_text = '文件传输助手'
pyperclip.copy(chinese_text)

# 切换到 PC 桌面
pyautogui.hotkey('win')
time.sleep(1)
# 找到微信并打开
pyautogui.typewrite('weix')
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)
# 在微信中找到“文件传输助手”，并输入“你好”2个字后点击发送按钮
pyautogui.click(x=1035, y=154)
time.sleep(1)
#pyautogui.typewrite(chinese_text)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=1290, y=618)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
#pyautogui.press('enter')

#pyautogui.press('enter')

# 延迟 2 秒，以便程序执行完毕
time.sleep(2)
