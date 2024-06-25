import pyautogui
import time
import pyperclip

# 将中文字符复制到剪贴板
#chinese_text = '文件传输助手'
#pyperclip.copy(chinese_text)
numbers = [1, 2]
for num in numbers:
    # 切换到 PC 桌面
    pyautogui.hotkey('win', 'd')
    time.sleep(1)
    #定位到3的目录
    pyautogui.press('3')
    time.sleep(1)
    #打开目录
    pyautogui.press('enter')
    time.sleep(3)
    #定位到word文件
    pyautogui.click(x=293, y=135)
    time.sleep(1)
    #打开word文件
    pyautogui.press('enter')
    time.sleep(5)
    #定位到word文件中
    pyautogui.click(x=1053, y=600)
    time.sleep(1)
    #全选word所有内容
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    #复制word所有内容
    pyautogui.hotkey('ctrl', 'c')
    #存储word文档内容
    context= pyperclip.paste()
    #打开浏览器
    pyautogui.click(x=171, y=1062)
    time.sleep(3)
    #找到对应页签
    pyautogui.click(x=313, y=58)
    chinese_text = 'https://tool.chinaz.com/Tools/jsonformat.aspx'
    pyperclip.copy(chinese_text)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=792, y=600)
    time.sleep(1)
    pyperclip.copy(context)
    pyautogui.hotkey('ctrl', 'v')
