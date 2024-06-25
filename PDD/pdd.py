import uiautomator2 as u2
import time
import os
import random
import CompareImages as comImg
def check_string_in_file(file_path, match_string):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if match_string in content:
        return True
    else:
        return False
def setPrice(price):
    coordinates = {
        '0': (0.366, 0.943),
        '1': (0.118, 0.725),
        '2': (0.382, 0.726),
        '3': (0.622, 0.725),
        '4': (0.118, 0.798),
        '5': (0.377, 0.8),
        '6': (0.617, 0.798),
        '7': (0.121, 0.871),
        '8': (0.369, 0.869),
        '9': (0.614, 0.872),
        '.': (0.121, 0.953)
    }
    #num = "6587.69"  # 假设要查询数字3.14的坐标
    price_int = float(price)
    price_int = round(price_int, 2)
    #计算下价格
    if price_int<5:
        price_int=12.9
    elif 5 <= price_int < 10:
        price_int=price_int*3
    elif 10 <= price_int < 30:
        price_int=price_int*2
    elif  price_int>=30:
        price_int=price_int*2.5
    print("最终价格："+str(price_int))
    for digit in str(price_int):
        if digit in coordinates:
            x_val, y_val = coordinates[digit]
            d.click(x_val,y_val)
            print(f"数字 {digit} 的坐标为：({x_val}, {y_val})")
        else:
            print(f"数字 {digit} 无对应的坐标信息")

def wirteFileInfo(title,price,img,url):
    filename = "C:/Users/Administrator/Desktop/33/pdd.txt"  # 指定文件名
    # 打开文件并写入数据
    with open(filename, "a") as file:
        line = str(title)+'|'+str(price)+'|'+str(img)+'|'+str(url) # 要写入的数据
        file.write(line + "\n")  # 写入数据并换行
    print("数据已写入文件。")
d = u2.connect_usb('v8eqhujjwwknkjyt')
print(d.info)
#点击全部商品
#d(resourceId="android:id/text1", text="全部商品").click()
#d(resourceId="com.xunmeng.pinduoduo:id/title", text="默认").click()
time.sleep(1)
iCs=1
iTdNum=0
while True:
    elem=d.xpath('//android.support.v4.view.ViewPager/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.view.ViewGroup['+str(iCs)+']/android.widget.FrameLayout[1]')
    elen1=d.xpath('//android.support.v4.view.ViewPager/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.view.ViewGroup['+str(iCs)+']')
    iSign=0
    if elen1.exists:
        iSign=1
    if elem.exists or iSign==1:
        #获取屏幕尺寸
        # screen_width, screen_height = d.window_size()
        #
        # #定义滑动起始点和终点坐标
        # start_x = screen_width // 2
        # start_y = screen_height // 2
        # end_x = start_x
        # end_y = screen_height // 4
        #
        # #执行向上滑动操作
        # d.swipe(0.173, 0.617, end_x, end_y-40, duration=0.4)

        #点击第一个商品
        if iSign==0:
            print("开始点击的商品"+str(iCs))
            d.xpath('//android.support.v4.view.ViewPager/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.view.ViewGroup['+str(iCs)+']/android.widget.FrameLayout[1]').click()
        else:
            print("开始点击分组的商品"+str(iCs))
            d.xpath('//android.support.v4.view.ViewPager/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.view.ViewGroup['+str(iCs)+']').click()
        time.sleep(1)
        title_text=""
        #获取标题对象
        elements=d(resourceId="com.xunmeng.pinduoduo:id/tv_title")
        title_text=elements.info["contentDescription"]
        if title_text=="":
            print('点击商品失败跳出')
            iCs=iCs+1
            time.sleep(2)
            continue
        if "使命召唤" in title_text:
            print('违规标题跳出'+elements.info["contentDescription"])
            d.xpath('//*[@content-desc="顶部工具栏"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
            iCs=iCs+1
            time.sleep(2)
            continue
        print('标题为'+elements.info["contentDescription"])

        if check_string_in_file("C:/Users/Administrator/Desktop/33/pdd.txt", title_text):
            print("商品："+title_text+"已存在跳出")
            #退回到店铺首页
            d.xpath('//*[@content-desc="顶部工具栏"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
            iCs=iCs+1
            time.sleep(2)
            continue
        pic_number=1
        # 获取图片的数量
        elements = d(resourceId="com.xunmeng.pinduoduo:id/pdd", index=2)
        print('图片数量'+elements.get_text())
        split_string = elements.get_text().split("/")
        if len(split_string) > 1:
            pic_number = split_string[1]
            print("斜杠后面的数字是:", pic_number)
        else:
            pic_number=1
            print("未找到斜杠后面的数字")
        time.sleep(1)

        #点击商品第一张图片
        d.click(0.498, 0.242)
        time.sleep(1)
        if d(resourceId="com.xunmeng.pinduoduo:id/pdd", description="播放").exists:
            d.swipe(0.738, 0.757, 0.138, 0.757, duration=0.1)
            time.sleep(1)
        #长按图片
        d.long_click(0.468, 0.472)
        #点击一键保存所有图片
        d.click(0.482, 0.774)
        time.sleep(10)
        #判断商品图片是否一样
        # if comImg.transfer_images_from_phone('/storage/emulated/0/DCIM/Pindd/goods/'):
        #     pic_number=1
        #点击关闭图片保存
        d.click(0.057, 0.075)

        time.sleep(2)
        #商品的价格
        elements = d(resourceId="com.xunmeng.pinduoduo:id/pdd")
        i=0
        iPrice=0
        price_text=""
        for ele in elements:
            price_text=ele.get_text()
            if "¥".lower() in price_text.lower():
                iPrice=iPrice+1
                continue
            if iPrice>0:
                price_text=ele.get_text()
                print('商品价格'+str(ele.get_text()))
                break
            if "/" in  price_text.lower() and pic_number==1 :
                split_string = price_text.split("/")
                if len(split_string) > 1:
                    pic_number = split_string[1]
                    print("斜杠后面的数字是:", pic_number)
        #点击复制商品地址
        d.click(0.939, 0.054)
        time.sleep(1)
        d.click(0.796, 0.828)
        time.sleep(3)
        # #点击客服
        # d(resourceId="com.xunmeng.pinduoduo:id/pdd", text="客服").click()
        # time.sleep(2)
        # d.long_click(0.382, 0.932)
        # time.sleep(2)
        # #粘贴地址
        # d(resourceId="android:id/floating_toolbar_menu_item_text", text="粘贴").click()
        # time.sleep(1)
        # print('商品地址查找')
        # elements = d(resourceId="com.xunmeng.pinduoduo:id/pdd")
        # url_text=""
        # i=0
        # for ele in elements:
        #     url_text=ele.get_text()
        #     if "https://".lower() in url_text.lower():
        #         print('商品地址'+str(i)+str(ele.get_text()))
        #         break
        #     i=i+1
        #去掉聊天里面的地址信息
        #d.long_click(0.432, 0.965)
        time.sleep(2)
        #点击全选
        #d(resourceId="android:id/floating_toolbar_menu_item_text", text="全选").click()
        #time.sleep(2)
        #d.click(0.344, 0.957)
        # d.click(0.236, 0.959)
        # time.sleep(2)
        # d.click(0.399, 0.963)
        # time.sleep(2)
        # #退回到商品首页
        # d(resourceId="com.xunmeng.pinduoduo:id/pdd", text="").click()

        #切换到记事本获取商品地址
        d.app_stop("com.miui.notes")
        d.app_start("com.miui.notes")
        time.sleep(3)
        d.click(0.848, 0.9)

        time.sleep(2)
        d.long_click(0.159, 0.278)
        time.sleep(2)
        #粘贴地址
        d(resourceId="android:id/floating_toolbar_menu_item_text", text="粘贴").click()

        elem=d(resourceId="com.miui.notes:id/rich_editor")
        time.sleep(2)
        url_text =elem.get_text()
        print(elem.get_text())
        #清空地址
        d(resourceId="com.miui.notes:id/undo").click()
        time.sleep(1)
        d.app_start("com.xunmeng.pinduoduo")
        time.sleep(1)
        #退回到店铺首页
        d.xpath('//*[@content-desc="顶部工具栏"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
        #重新打开咸鱼
        d.app_stop("com.taobao.idlefish")
        #d.app_start("com.taobao.idlefish")
        d.press('home')
        time.sleep(2)
        d.swipe(0.738, 0.757, 0.138, 0.757, duration=0.1)
        time.sleep(2)
        #d.app_start("com.taobao.idlefish")
        elem=d.xpath('//*[@resource-id="com.miui.home:id/workspace"]/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.TextView[1]')
        if elem.exists:
            if "闲鱼" in elem.get_text():
                d.click(0.132, 0.087)
                time.sleep(1)
            else:
                print("无法打开闲鱼")
        else:
            print("无法打开闲鱼")

        time.sleep(2)
        #点击卖闲置
        d.click(0.493, 0.942)
        time.sleep(2)
        d.click(0.358, 0.8)
        time.sleep(1)
        d.click(0.107, 0.134)
        try:
            print("输入标题："+title_text)
            d.send_keys(title_text)
        except Exception as e:
            print(f"发生请求异常：{str(e)}")
        except Exception as e:
            print(f"发生错误：{str(e)}")
        iTitle=1
        while True:
            if d(description=title_text).exists:
                break
            print("等待输入标题内容")
            time.sleep(5)
            iTitle=iTitle+1
            if iTitle>10:
                d.app_start("com.xunmeng.pinduoduo")
                break

        time.sleep(1)
        d(description="添加图片").click()
        time.sleep(2)

        #选择图片
        # d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ImageView[2]/android.view.View[1]').click()
        # if int(pic_number)>1:
        #     for i in range(3,int(pic_number)+2):
        #         time.sleep(1)
        #         d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ImageView['+str(i)+']/android.view.View[1]').click()
        #         i=i+1
        d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ImageView['+str(int(pic_number)+1)+']/android.view.View[1]').click()
        if int(pic_number)>1:
            for i in range(int(pic_number),1,-1):
                time.sleep(1)
                d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ImageView['+str(i)+']/android.view.View[1]').click()
        time.sleep(1)
        #选择图片后点击下一步
        if int(pic_number)<=9:
            d(description="下一步 ("+str(pic_number)+")").click()
        else:
            d(description="下一步 (9)").click()
        time.sleep(2)
        d(description="完成").click()
        time.sleep(3)

        #点击分类、品牌、尺寸等书籍
        # if d(description="游戏其他").exists:
        #     d(description="游戏其他").click()
        # else :
        #     x,y = d(description='PS游戏光盘/软件').center()
        #     d.swipe(0.575, 0.466, 0.289, 0.466, duration=0.2)
        #     time.sleep(1)
        #     if d(description="游戏其他").exists:
        #         d(description="游戏其他").click()
        #     else :
        #         d.click(0.393, 0.751)
        # time.sleep(1)
        i=1
        iSetPrice=0
        iSetMail=0
        iQc=0
        for i in range(1,5):
            d.swipe(0.338, 0.757, 0.338, 0.557, duration=0.4)
            time.sleep(1)
            if d(description="全新").exists and iQc<1:
                d(description="全新").click()
                iQc=1
                time.sleep(1)
            if d(description="价格设置").exists and iSetPrice<1:
                d(description="价格设置").click()
                time.sleep(2)
                #本手机账号点击输入价格
                #d.click(0.209, 0.591)
                #d.click(0.876, 0.909)
                #1272账号点击输入价格
                d.click(0.206, 0.469)
                time.sleep(1)
                setPrice(price_text)
                d(description="确定").click()
                iSetPrice=iSetPrice+1
                time.sleep(2)
                if d(description="同步宝贝到圈子").exists and iSetMail<1:
                    #d.click(0.457, 0.8)
                    #d.click(0.699, 0.708)
                    #获取发货方式的地址坐标
                    element = d(description="同步宝贝到圈子")
                    x, y = element.center()    # 获取元素中心点坐标
                    d.click(x,y-70)
                    time.sleep(1)
                    d(description="包邮").click()
                    time.sleep(1)
                    d(description="确定").click()
                    # time.sleep(2)
                    # d.swipe(0.338, 0.757, 0.338, 0.557, duration=0.2)
                    # time.sleep(2)
                    # d.click(0.104, 0.806)
                    iSetMail=iSetMail+1
                #点击发货按钮
            time.sleep(1)
        #点击发布
        d(description="发布").click()
        time.sleep(3)
        wirteFileInfo(title_text,price_text,pic_number,url_text)
        print("点击完成的商品"+str(iCs))
        iCs=iCs+1
        if iCs>30:
            break
        d.app_start("com.xunmeng.pinduoduo")
        number = random.uniform(5, 20)
        print("等待"+str(number)+'秒')
        time.sleep(number)
    else:
        number = random.uniform(0.1, 1)
        d.swipe(0.165, 0.619, 0.165, 0.398, duration=number)
        print("拖动商品"+str(iCs))
        time.sleep(3)
        if iTdNum>2:
            iCs=3
            iTdNum=0
        iTdNum=iTdNum+1