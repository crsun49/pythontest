
import time
import uiautomator2 as u2
import opporequestshtml as a
import  ImageConversion as imgCon
d = u2.connect_usb('v8eqhujjwwknkjyt')
print(d.info)
d.xpath('//*[@resource-id="android:id/list"]/android.view.ViewGroup[7]').long_click()