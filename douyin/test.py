
import time
import uiautomator2 as u2
import opporequestshtml as a
import  ImageConversion as imgCon
d = u2.connect_usb('v8eqhujjwwknkjyt')
print(d.info)
time.sleep(1)
#点击手机
d.xpath('//android.widget.HorizontalScrollView/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]').click()
time.sleep(1)
#点击目录1
d.xpath('//*[@resource-id="android:id/list"]/android.view.ViewGroup[1]').click()
#pushFiles(d,1,'5731','D:/JAVA/UploadFile/xbgame/Images/5731.jpg','D:/JAVA/UploadFile/xbgame/Videos/5731.mp4')