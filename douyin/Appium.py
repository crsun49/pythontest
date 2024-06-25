import os
import time

import uiautomator2 as u2
#d = u2.connect_usb('HYC5T20109001239')
d = u2.connect_usb('498f62e8')
print(d.info)
# 执行adb shell命令来打开指定目录
d.app_stop("com.huawei.filemanager")
# 关闭应用程序（这里使用“文件管理器”应用程序作为示例）
d.app_start("com.huawei.filemanager")
time.sleep(1)
#d(resourceId='com.huawei.filemanager:id/layout_file_detail').click()
d.click(0.151, 0.421)
time.sleep(2)
d(resourceId='com.huawei.filemanager:id/file_info_view')[1].click()
time.sleep(2)
#长按第一个视频
#d.long_click(0.609, 0.262)
#长按第二个视频
d.long_click(0.431, 0.35)
time.sleep(1)
#点击分享按钮
d.click(0.099, 0.979)
time.sleep(2)
#点击抖音按钮
d.click(0.12, 0.757)
time.sleep(2)
#点击发布
d.click(0.28, 0.615)
time.sleep(5)
#去掉配置音乐
d.click(0.759, 0.072)
time.sleep(1)
#点击下一步
d.click(0.732,0.96)
time.sleep(2)
d.click(0.167, 0.171)
time.sleep(1)
#复制内容
#d.set_fastinput_ime(False)
d.send_keys("steam游戏")
#d.set_fastinput_ime(true)
time.sleep(6)
# #长按文本框
# d.long_click(0.169, 0.171)
# time.sleep(1)
# #点击粘贴
# d.click(0.12, 0.094)
#点击高级设置
d.click(0.206, 0.804)
time.sleep(1)
#去掉运行下载
d.click(0.882, 0.675)
time.sleep(1)
#回到发布界面
d.click(0.169, 0.171)
#点击公开设置
d.click(0.395, 0.595)
#设置仅自己可见
d.click(0.335, 0.969)
#回到发布界面
d.click(0.169, 0.171)
time.sleep(1)
#点击选择封面
d.click(0.819, 0.256)
time.sleep(4)
d.drag(0.083, 0.938, 0.492, 0.94, duration=0.5)
time.sleep(7)
#封面设置下一步
d.click(0.835, 0.071)
#保存封面
d.click(0.835, 0.071)

