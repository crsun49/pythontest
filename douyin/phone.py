import os
import time

import uiautomator2 as u2

d = u2.connect_usb('498f62e8')
#d = u2.connect_usb('HYC5T20109001239')




#d.app_start('com.tencent.weread')
# 连接设备
print(d.info)
d.app_stop('com.taobao.idlefish')
time.sleep(2)
# #打开微信
# d.app_start('com.tencent.mm')
#打开xy
d.app_start('com.taobao.idlefish')
time.sleep(2)
# #等待元素出现
d.implicitly_wait(3)
# d(resourceId='com.tencent.mm:id/bth').click();
# print(d(resourceId='com.tencent.mm:id/knx').get_text())
d.click(0.502, 0.954)
time.sleep(1)
#d.click(0.518, 0.903)
d.click(0.458, 0.811)
time.sleep(2)
d.click(0.35, 0.179)
time.sleep(1)
#element =d(description="描述, 描述一下宝贝的品牌型号、货品来源…")
#d(description="描述, 描述一下宝贝的品牌型号、货品来源…").click()
d.click(0.193, 0.185)
time.sleep(2)
#d.set_fastinput_ime(True)
#d.send_keys("#steam游戏")
#d(focused=True).set_text("1212")
d(description="描述, 描述一下宝贝的品牌型号、货品来源…").set_text("2434343")
#
#d.set_fastinput_ime(True)
#d.send_keys("你好撒的飞送的飞送的")
#d(description="描述, 描述一下宝贝的品牌型号、货品来源…").set_text("34234")
#d.set_fastinput_ime(False)
#
# #element[0].send_keys('asdasjjjj55555d66666',True)
# d.press("ctrl+v")
# time.sleep(1)
# d.press("ctrl+v")
# d(focused=True).set_text('asdasjjjj55555d66666')
# 切换成FastInputIME输入法
# d.set_fastinput_ime(True)
# # adb广播输入


