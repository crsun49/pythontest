
import time
import uiautomator2 as u2
import opporequestshtml as a
import  ImageConversion as imgCon
import os
def pushFiles(d,fileName,pathname):
    # # 电脑上源文件路径和手机上目标路径 C:\Users\Administrator\Desktop\33 C:/Users/ODC/Desktop/33/

    source_file_path_img = "C:/Users/"+pathname+"/Desktop/33/"+fileName+".jpg"
    source_file_path_video = "C:/Users/"+pathname+"/Desktop/33/"+fileName+".MP4"
    target_directory_video = "/sdcard/1/"
    target_directory_img = "/sdcard/DCIM/Camera/"
    #推送图片
    source_directory = "C:/Users/Administrator/Desktop/33"
    d.push(source_file_path_img, target_directory_img)
    #推送视频
    d.push(source_file_path_video, target_directory_video)
    # 获取目录中的所有 JPG 文件
    # jpg_files = [file for file in os.listdir(source_directory) if file.lower().endswith(".jpg")]
    # # 遍历 JPG 文件并推送到手机上
    # i=0
    # for jpg_file in jpg_files:
    #     source_file_path = os.path.join(source_directory, jpg_file)
    #     d.push(source_file_path, target_directory)

    #推送成功后刷新相册列表
    d.shell("am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/")
    print("文件推送成功")
def faDouYin(url,i,pathname,zwtitle):
    #下载图片和视频到电脑
    #title = a.main("https://byrut.org/4455-left-4-dead-2.html", '0')
    title = a.main(url, str(i))
    if title=='-1' or title=='':
        print('图片抓取失败')
        return '1'
    #title="Left4De ad2"
    time.sleep(2)
    #将低分辨率的图片转换成高分辨率
    imgCon.imgConversion("C:/Users/"+pathname+"/Desktop/33/"+str(i)+".jpg", "C:/Users/"+pathname+"/Desktop/33/"+str(i)+".jpg")
    time.sleep(2)
    d = u2.connect_usb('v8eqhujjwwknkjyt')
    print(d.info)
    #推送文件到手机
    pushFiles(d, str(i) ,pathname)
    time.sleep(3)
    # 执行adb shell命令来打开指定目录
    #关闭抖音和文件管理
    d.app_stop("com.coloros.filemanager")
    d.app_stop('com.ss.android.ugc.aweme')
    # 关闭应用程序（这里使用“文件管理器”应用程序作为示例）
    d.app_start("com.coloros.filemanager")
    time.sleep(1)
    #点击内存存储
    d.click(0.435, 0.282)
    time.sleep(1)
    #点击目录1
    d.click(0.435, 0.282)
    time.sleep(1)
    #长按第二个视频
    #d.long_click(0.36, 0.279)
    d.long_click(0.553, 0.266+(i*0.077))
    time.sleep(1)
    #点击分享按钮
    d.click(0.099, 0.979)
    time.sleep(2)
    #点击抖音按钮
    d.click(0.149, 0.859)
    time.sleep(3)
    #点击下一步
    d.click(0.815, 0.923)
    time.sleep(2)
    # d.click(0.167, 0.171)
    # time.sleep(1)
    #复制内容
    #d.set_fastinput_ime(False)
    try:
        d.send_keys("#"+zwtitle.replace(" ","")+" #"+title.replace(" ",""))
    except Exception as e:
        print(f"发生请求异常：{str(e)}")
    except Exception as e:
        print(f"发生错误：{str(e)}")
    #d.set_fastinput_ime(true)
    time.sleep(3)
    print('复制内容')
    #切换到设置界面
    d.click(0.917, 0.675)
    #点击高级设置
    #d.click(0.334, 0.565)
    if d(text='高级设置').exists:
        d(text='高级设置').click()
    else:
        d.click(0.916, 0.672)
        time.sleep(2)
        d(text='高级设置').click()

    time.sleep(2)
    #去掉允许下载
    #d.click(0.898, 0.66)
    d(text='允许下载').click()
    time.sleep(1)
    #回到发布界面
    d.click(0.169, 0.171)
    # #点击公开设置
    # d.click(0.395, 0.595)
    # #设置仅自己可见
    # d.click(0.335, 0.969)
    # #回到发布界面
    # d.click(0.169, 0.171)
    time.sleep(1)
    #点击选择封面
    d.click(0.866, 0.238)
    time.sleep(3)
    #切换竖版
    d.click(0.791, 0.583)
    time.sleep(2)
    #点击想相册选择封面
    d.click(0.887, 0.907)
    time.sleep(3)
    #选择第一张相片
    d.click(0.157, 0.18)
    time.sleep(2)
    # #点击下一步
    d.click(0.836, 0.072)
    time.sleep(4)
    #点击保存封面
    d.click(0.836, 0.073)
    time.sleep(2)
    #添加小程序
    d(text='添加小程序').click()
    time.sleep(2)
    d(resourceId="com.ss.android.ugc.aweme:id/x3t", text="懂车帝").click()
    #(0.252, 0.386)
    time.sleep(3)
    #短视频任务
    if not d(text='短视频任务').exists:
        time.sleep(4)
        d(text="短视频任务").click()
    else:
        d(text="短视频任务").click()
    time.sleep(4)
    #打开全部车型
    #d.click(0.252, 0.386)
    d(text="全部车型").click()
    if d(resourceId="_Di").exists:
        d(resourceId="_Di").click()
        time.sleep(1)
    else:
        time.sleep(3)
        d(resourceId="_Di").click()
    time.sleep(2)
    #选择B
    d(resourceId="dic-B").click()
    time.sleep(2)
    if d(text='比亚迪').exists:
        d(text='比亚迪').click()
        time.sleep(1)
        d(text='海鸥').click()
        time.sleep(1)
    else:
        d.click(0.352, 0.386)
        d.click(0.652, 0.386)
    d(text="将此页添加到视频").click()
    time.sleep(3)
    #点击发布
    d.click(0.766, 0.943)
    time.sleep(50)
    #点击全部车型
    # 输出文件内容
    ##删除指定目录文件
    # print("删除图片和视频")
    #d.shell(f"rm /sdcard/1/0.mp4")
    # 使用 adb_shell 方法在设备上执行 rm 命令，删除目录中的所有 JPG 文件
    #d.shell(f"rm /sdcard/DCIM/Camera//0.jpg")
    print("执行成功")
#'https://byrut.org/15896-the-elder-scrolls-5-skyrim.html',
my_url = [
   'https://thebyrut.org/2325-europa-universalis-4.html']
i =0
pathname ="Administrator"
my_zwtitle=['欧陆风云4']
# 使用循环遍历数组中的元素
ics=0
for url in my_url:
    try:
        faDouYin(my_url[i], i , pathname,my_zwtitle[i])
        i=i+1
        print(f"成功-"+str(i))
    except Exception as e:
        print(f"发生请求异常：{str(e)}")
        if ics > 2:
            i=i+1
        ics=ics+1
    except Exception as e:
        print(f"发生错误：{str(e)}")
        if ics > 2:
            i=i+1
        ics=ics+1
print('全部执行完成')




