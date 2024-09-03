
import time
import uiautomator2 as u2
import douyin.opporequestshtml as a
import  douyin.ImageConversion as imgCon
import ConSQL.ConSQL as con
import ffmpeg
import douyin.gameclick as game
import os
def pushFiles(d,Num,fileName,imgFilePath,videoFilePath):
    # # 电脑上源文件路径和手机上目标路径 C:\Users\Administrator\Desktop\33 C:/Users/ODC/Desktop/33/

    #source_file_path_img = "D:/JAVA/UploadFile/xbgame/Images/"+fileName+".jpg"
    #source_file_path_video = "C:/Users/"+pathname+"/Desktop/33/"+fileName+".MP4"
    target_directory_video = "/sdcard/1/"
    target_directory_img = "/sdcard/DCIM/Camera/"
    #推送图片
    #source_directory = "C:/Users/Administrator/Desktop/33"
    d.push(imgFilePath, target_directory_img)
    #推送视频
    d.push(videoFilePath, target_directory_video)
    time.sleep(2)
    old_img_file_path = f"{target_directory_img}{fileName}.jpg"
    new_img_file_path = f"{target_directory_img}{str(Num)}.jpg"

    #d.shell(f"mv {old_img_file_path} {new_img_file_path}")
    old_video_file_path = f"{target_directory_video}{fileName}.MP4"
    new_video_file_path = f"{target_directory_video}{str(Num)}.MP4"
    d.shell(f"mv {old_video_file_path} {new_video_file_path}")
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
def delFiles(d,i):
    d.shell(f"rm /sdcard/1/"+str(i-3)+".mp4")
def faDouYin(d,game,i):
    #下载图片和视频到电脑
    #title = a.main("https://byrut.org/4455-left-4-dead-2.html", '0')
    #title = a.main(url, str(i))
    if game.title=='-1' or game.title=='':
        print('图片抓取失败')
        return '1'
    #title="Left4De ad2"
    time.sleep(2)
    #将低分辨率的图片转换成高分辨率
    imgCon.imgConversion(game.imgFilePath, game.imgFilePath)
    time.sleep(2)
    #d = u2.connect_usb('v8eqhujjwwknkjyt')
    print(d.info)
    #判断MP4文件是否存在不存在则转换
    if not os.path.isfile(game.videoFilePath):
        ffmpeg.input(pathImg+game.filename+'.webm').output(game.videoFilePath).run()
    #推送文件到手机
    pushFiles(d, str(i) ,game.filename,game.imgFilePath,game.videoFilePath)
    time.sleep(3)
    # 执行adb shell命令来打开指定目录
    #关闭抖音和文件管理
    d.app_stop("com.android.fileexplorer")
    d.app_stop('com.ss.android.ugc.aweme')
    # 关闭应用程序（这里使用“文件管理器”应用程序作为示例）
    d.app_start("com.android.fileexplorer")
    time.sleep(1)
    #点击手机
    d.xpath('//android.widget.HorizontalScrollView/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]').click()
    time.sleep(1)
    #点击目录1
    d.xpath('//*[@resource-id="android:id/list"]/android.view.ViewGroup[1]').click()
    time.sleep(1)
    #d.long_click(0.36, 0.266+(i*0.077))
    #d(resourceId="com.android.fileexplorer:id/file_name", text=""+str(i)+".MP4")
    time.sleep(1)
    #如果i>9就删除
    if i>8:
        delFiles(d,i)
        time.sleep(2)
        d.xpath('//*[@resource-id="android:id/list"]/android.view.ViewGroup[9]').long_click()
    else:
        d.xpath('//*[@resource-id="android:id/list"]/android.view.ViewGroup['+str(i+1)+']').long_click()
    time.sleep(1)
    #点击发送按钮
    d.xpath('//*[@content-desc="发送"]/android.widget.ImageView[1]').click()
    time.sleep(2)
    #点击抖音按钮
    #d.click(0.159, 0.655)
    d.click(0.129, 0.893)
    time.sleep(2)
    ixh=0
    while True:
        if d(text='下一步').exists:
            break  # 当条件满足时跳出循环
        else:
            print('循环第'+str(ixh))
            ixh=ixh+1
            time.sleep(2)

    #点击下一步
    d(text='下一步').click()
    time.sleep(2)
    try:
        #点击文本框
        d.set_fastinput_ime(True)
        d.click(0.184, 0.123)
        d.send_keys(("" if game.gameNameCh.replace(" ","") in game.gameintroduce.replace(" ","") else game.gameNameChstr.replace(" ",""))+game.gameintroduce.replace(" ","")+" "+" #"+game.gameNameCh.replace(" ","")+" #"+game.gameName.replace(" ",""))
        d.set_fastinput_ime(False)
    except Exception as e:
        print(f"发生请求异常：{str(e)}")
    except Exception as e:
        print(f"发生错误：{str(e)}")
    #d.set_fastinput_ime(true)
    time.sleep(2)
    print('复制内容')
    #切换到设置界面
    d.click(0.917, 0.675)
    #点击高级设置
    #d.click(0.334, 0.565)
    if d(text='高级设置').exists:
        d(text='高级设置').click()
    else:
        d.click(0.922, 0.611)
        time.sleep(1)
        d.click(0.922, 0.611)
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
    d.click(0.776, 0.211)
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

    #
    # #添加小程序
    # d(text='小程序 或 游戏').click()
    # time.sleep(2)
    # d(text='小程序').click()
    # print("小程序")
    # time.sleep(2)
    # d(resourceId="com.ss.android.ugc.aweme:id/yfj", text="懂车帝").click()
    # time.sleep(3)
    # #短视频任务
    # if not d(text='短视频任务').exists:
    #     time.sleep(4)
    #     d(text="短视频任务").click()
    # else:
    #     d(text="短视频任务").click()
    # time.sleep(4)
    # #打开全部车型
    # #d.click(0.252, 0.386)
    # d(text="全部车型").click()
    # # if d(resourceId="_Di").exists:
    # #     d(resourceId="_Di").click()
    # #     time.sleep(1)
    # # else:
    # #     time.sleep(3)
    # #     d(resourceId="_Di").click()
    # time.sleep(2)
    # #选择B
    # d(resourceId="dic-B").click()
    # time.sleep(2)
    # if d(text='比亚迪').exists:
    #     d(text='比亚迪').click()
    #     time.sleep(1)
    #     d(text='海鸥').click()
    #     #比亚迪e3 秦EV海鸥
    #     time.sleep(1)
    # else:
    #     d.click(0.352, 0.386)
    #     d.click(0.652, 0.386)
    #
    #
    #
    # d(text="将此页添加到视频").click()
    # time.sleep(3)
    #
    #
    #
    #点击发布
    d.click(0.766, 0.943)
    time.sleep(4)
    ixh=0
    while True:
        if d(resourceId="com.ss.android.ugc.aweme:id/ehe").exists or ixh<60 :
            print('循环第'+str(ixh)+'等带发布')
            ixh=ixh+1
            time.sleep(2)
        else:
            print('循环第跳出')
            break  # 当条件满足时跳出循环
    return 'true'

    #点击全部车型
    # 输出文件内容
    ##删除指定目录文件
    # print("删除图片和视频")
    #d.shell(f"rm /sdcard/1/0.mp4")
    # 使用 adb_shell 方法在设备上执行 rm 命令，删除目录中的所有 JPG 文件
    #d.shell(f"rm /sdcard/DCIM/Camera//0.jpg")
    print("执行成功")
#'https://byrut.org/15896-the-elder-scrolls-5-skyrim.html',
# my_url = [
#
#   'https://thebyrut.org/443-middle-earth-shadow-of-war-definitive-edition.html', 'https://thebyrut.org/6584-postal-2.html', 'https://thebyrut.org/8837-elite-dangerous.html', 'https://thebyrut.org/1867-xcom-2.html', 'https://thebyrut.org/1408-fallout-76.html', 'https://thebyrut.org/7741-gunfire-reborn.html', 'https://thebyrut.org/3417-hotline-miami.html', 'https://thebyrut.org/3601-mirror.html', 'https://thebyrut.org/16291-total-war-warhammer-3.html', 'https://thebyrut.org/6508-metal-gear-solid-5-the-phantom-pain.html', 'https://thebyrut.org/735-dark-souls-remastered.html', 'https://thebyrut.org/1705-grim-dawn.html', 'https://thebyrut.org/1437-tekken-7.html', 'https://thebyrut.org/4106-mortal-kombat-11-ultimate-edition.html', 'https://thebyrut.org/23887-starfield.html', 'https://thebyrut.org/6148-half-life-alyx.html', 'https://thebyrut.org/3083-middle-earth-shadow-of-mordor.html'
# ]
# i =0
# pathname ="Administrator"
# my_zwtitle=[  '生化危机4重制版', '中土世界：战争之影-终极版', '邮差2', '精英危险', 'XCOM 2', '辐射76', '火枪行动', '热线迈阿密', '镜像', '全面战争：战锤3', '合金装备5：幻痛', '黑暗之魂重制版', '孤城黎明', '铁拳7', '真人快打11终极版', '星际战甲', '半条命：艾丽克斯', '中土世界：魔多之影']
# # 使用循环遍历数组中的元素
# ics=0
# for url in my_url:
#     try:
#         faDouYin(my_url[i], i , pathname,my_zwtitle[i].replace('&#039;','').replace(':',' '))
#         i=i+1
#         print(f"成功-"+str(i))
#     except Exception as e:
#         print(f"发生请求异常：{str(e)}")
#         if ics > 2:
#             i=i+1
#         ics=ics+1
#     except Exception as e:
#         print(f"发生错误：{str(e)}")
#         if ics > 2:
#             i=i+1
#         ics=ics+1
# print('全部执行完成')
pathImg="D:/JAVA/UploadFile/xbgame/Images/"
def Main():
    db = con.SQLServerDB()
    query = "select top 10 * from dbo.p_xbgame where status= ? AND isTs=?"
    params = (1,0)
    d = u2.connect_usb('v8eqhujjwwknkjyt')
    xbgames=db.fetch_data(query, params)
    i=0
    for game in xbgames:
        #pushFiles(d,i,game.filename,game.imgFilePath,game.videoFilePath)
        rtn=faDouYin(d,game,i)
        #rtn= "true"
        if rtn == "true":
            print('发布成功'+str(game.gameNameCh))
            update_dict = {'isTs': 1}
            # 条件设置为 id = ?
            condition = 'id = ?'
            # 实际参数值，这里假设你要更新 id 为 123 的记录
            params = [game.id]
            # 执行更新操作
            db.update_data('p_xbgame', update_dict, condition, params)
        i=i+1
Main()
#ffmpeg.input('D:/JAVA/UploadFile/xbgame/Videos/2551.webm').output('D:/JAVA/UploadFile/xbgame/Videos/2551.mp4').run()
#d = u2.connect_usb('v8eqhujjwwknkjyt')
#d.app_stop("com.android.fileexplorer")
#d.app_stop('com.ss.android.ugc.aweme')
#d.app_stop("com.taobao.idlefish")
#d.app_start("com.taobao.idlefish")


