import time
def gameclick1(d):
    #添加小程序
    d(text='小程序 或 游戏').click()
    time.sleep(2)
    d(text='游戏').click()
    print("小程序")
    time.sleep(3)
    #点击角色
    d.click(0.462, 0.234)
    #点击第一个游戏
    d.click(0.859, 0.312)
    time.sleep(3)
def gamelick2(d):
    #添加小程序
    d(text='小程序 或 游戏').click()
    time.sleep(2)
    d(text='游戏').click()
    print("小程序")
    time.sleep(3)
    #点击角色
    d.click(0.462, 0.234)
    time.sleep(3)
    #点击第一个游戏
    d.click(0.859, 0.312)
    time.sleep(3)