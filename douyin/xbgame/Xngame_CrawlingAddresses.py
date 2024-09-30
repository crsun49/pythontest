#抓取对应网站的标题和图片、详细地址信息并且下载图片到指定位置
import requests
import common.DownloadImage as downimg
from bs4 import BeautifulSoup
import os
import json
import re
from datetime import datetime
import uuid
import ConSQL.ConSQL as con
import common.CommonMethods as math
import douyin.opporequestshtml as a
import ffmpeg
import subprocess
class Game:
    def __init__(self, title,gameName,gameNameCh, href,imgsrc,videosrc , gameintroduce,status,createtime,imgFilePath,videoFilePath,filename,isTs):
        self.title = title
        self.gameName = gameName
        self.gameNameCh = gameNameCh
        self.href = str(href)
        self.filename = filename
        self.imgsrc = str(imgsrc)
        self.videosrc = videosrc
        self.gameintroduce =gameintroduce
        self.status = status
        self.isTs = isTs
        self.createtime = createtime
        self.imgFilePath = imgFilePath
        self.videoFilePath = videoFilePath
    def __str__(self):
        return f"标题: {self.title}\n图片地址: {self.imgsrc}\n详细地址: {self.href}\n游戏介绍: {self.gameintroduce}\n"

    def to_dict(self):
        return {
            'title': self.title,
            'gameName': self.gameName,
            'gameNameCh': self.gameNameCh,
            'filename': self.filename,
            'href': self.href,
            'imgsrc': str(self.imgsrc),
            'videosrc': self.videosrc,
            'gameintroduce': self.gameintroduce,
            'status': self.status,
            'isTs': self.isTs,
            'createtime': self.createtime,
            'imgFilePath': self.imgFilePath,
            'videoFilePath': self.videoFilePath
        }
def requests_gamepostlist(page):
    # 定义不允许出现的字符（这里以<>:"/\|?*为例）
    header_param = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Cookie': 'darkStyle=1; gg_info=1720663227'
    }
    response = requests.get('https://www.xbgame.net/pcgame/pcgame-1/page/'+str(page), proxies=proxies)  # 发送HTTP GET请求
    soup = BeautifulSoup(response.text, 'html.parser')  # 解析HTML文档

    # hrefs = []   #详细地址数组
    # titles = []  #标题数据组
    # srcs = []    #图片地址
    # game_ntroduce=[] #游戏介绍

    # 创建游戏对象列表

    # 找到所有 class="post-list-item item-post-style-1" 的元素
    boxes = soup.find_all(class_="post-list-item item-post-style-1")
    count = 1  # 计数器初始化
    for box in boxes:
        # if count <0:
        #     count += 1
        #     continue  # 当计数器等于3时跳出循环
        pattern = r'item-(\d+)'
        match = re.search(pattern, str(box))
        filename=match.group(1)
        if filename=="":
            continue
        img_tag=box.find("img", class_="post-thumb" , alt=True, src=True)
        a_tag=box.find("a", class_="thumb-link", href=True)
        # match = re.search(r'apps/(\d+)/', img_tag['src'].split('?')[0])
        # filename=""
        # if match:
        #     filename = match.group(1)  # 获取匹配到的数字部分
        math.generate_random_number(1,5,2)
        gameintroduce,videourl=get_game_introduce(a_tag['href'].split('?')[0])
        math.generate_random_number(1,5,2)
        #下载图片到指定目录
        if not os.path.isfile(pathImg+filename+'.jpg'):
            downimg.download_image_proxies(img_tag['src'].split('?')[0],pathImg+filename+'.jpg',proxies)
        match = re.search(r'apps/(\d+)/', img_tag['src'].split('?')[0])
        videofilename=""
        if match:
            videofilename = match.group(1)  # 获取匹配到的数字部分
        #获取中英文名字
        gameNameCh,gameName = extract_names(img_tag['alt'])
        #下载视频到指定目录
        if not os.path.isfile(pathVideo+filename+'.mp4'):
            downimg.download_image_proxies(videourl,pathVideo+filename+'.webm',proxies)
            #将webm格式转换mp4
            #ffmpeg.input(pathVideo+filename+'.webm').output(pathVideo+filename+'.mp4').run()
            convert_webm_to_mp4(pathVideo+filename+'.webm',pathVideo+filename+'.mp4')
        math.generate_random_number(1,5,2)
        #return
        games = []
        game = Game(img_tag['alt'],gameName,gameNameCh, a_tag['href'].split('?')[0], img_tag['src'].split('?')[0], videourl,gameintroduce,1,datetime.now(),pathImg+filename+'.jpg',pathVideo+filename+'.mp4',filename,0)
        games.append(game)
        insert_game_data(games)
        count += 1  # 每次循环计数器加1
        print('第'+str(count))
        if count>15 :
            return

    #将抓取的数据存储到数据库
    # data_to_insert  = [(uuid.uuid4(),game.title,game.gameName,game.gameNameCh,game.href,game.imgsrc,game.videosrc,game.gameintroduce,game.status,game.createtime,game.imgFilePath,game.videoFilePath,game.filename,0) for game in games]
    # db = con.SQLServerDB()
    # db.insert_data('p_xbgame', ['id','title','gameName','gameNameCh', 'herf', 'imgsrc', 'videosrc', 'gameintroduce','status','createtime','imgFilePath','videoFilePath','filename','isTs'], data_to_insert)
    # print("执行数据成功")
    # 创建一个集合来存储已存在的 videoFilePath
    # existing_video_file_paths = []
    # db = con.SQLServerDB()
    # # 查询数据库，检查哪些 videoFilePath 已经存在
    # query = "SELECT videoFilePath FROM dbo.p_xbgame WHERE videoFilePath IN ({})".format(
    #     ','.join(['?' for _ in range(len(games))])
    # )
    # video_file_paths_to_check = [game.videoFilePath for game in games]
    # existing_video_file_paths_result = db.fetch_data(query, video_file_paths_to_check)
    #
    # for row in existing_video_file_paths_result:
    #     existing_video_file_paths.append(row[0])
    #
    # # 准备要插入的数据
    # data_to_insert = [
    #     (
    #         uuid.uuid4(),
    #         game.title,
    #         game.gameName,
    #         game.gameNameCh,
    #         game.href,
    #         game.imgsrc,
    #         game.videosrc,
    #         game.gameintroduce,
    #         game.status,
    #         game.createtime,
    #         game.imgFilePath,
    #         game.videoFilePath,
    #         game.filename,
    #         0
    #     )
    #     for game in games
    #     if game.videoFilePath not in existing_video_file_paths
    # ]
    #
    # # 执行插入操作
    # if data_to_insert:
    #     db.insert_data(
    #         'p_xbgame',
    #         ['id', 'title', 'gameName', 'gameNameCh', 'href', 'imgsrc', 'videosrc', 'gameintroduce', 'status', 'createtime', 'imgFilePath', 'videoFilePath', 'filename', 'isTs'],
    #         data_to_insert
    #     )
    #     print("数据插入成功")
    # else:
    #     print("没有需要插入的数据")
def convert_webm_to_mp4(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx264',  # 视频编码
        '-preset', 'slow',   # 编码速度，可能根据需要选择
        '-crf', '28',        # 质量控制
        '-threads', '1',     # 限制线程数以减少 CPU 使用率
        output_file
    ]
    subprocess.run(command)
def insert_game_data(games):
    existing_video_file_paths = []
    db = con.SQLServerDB()
    # 查询数据库，检查哪些 videoFilePath 已经存在
    query = "SELECT videoFilePath FROM dbo.p_xbgame WHERE videoFilePath IN ({})".format(
        ','.join(['?' for _ in range(len(games))])
    )
    video_file_paths_to_check = [game.videoFilePath for game in games]
    existing_video_file_paths_result = db.fetch_data(query, video_file_paths_to_check)

    for row in existing_video_file_paths_result:
        existing_video_file_paths.append(row[0])

    # 准备要插入的数据
    data_to_insert = [
        (
            uuid.uuid4(),
            game.title,
            game.gameName,
            game.gameNameCh,
            game.href,
            game.imgsrc,
            game.videosrc,
            game.gameintroduce,
            game.status,
            game.createtime,
            game.imgFilePath,
            game.videoFilePath,
            game.filename,
            0
        )
        for game in games
        if game.videoFilePath not in existing_video_file_paths
    ]

    # 执行插入操作
    if data_to_insert:
        db.insert_data(
            'p_xbgame',
            ['id', 'title', 'gameName', 'gameNameCh', 'href', 'imgsrc', 'videosrc', 'gameintroduce', 'status', 'createtime', 'imgFilePath', 'videoFilePath', 'filename', 'isTs'],
            data_to_insert
        )
        print("数据插入成功")
    else:
        print("没有需要插入的数据")
#获取游戏介绍文本
def get_game_introduce(url):
    # 定义不允许出现的字符（这里以<>:"/\|?*为例）
    header_param = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Cookie': 'darkStyle=1; Hm_lvt_36ae7161b950fe10c9fec864cb79c1d2=1720252327; HMACCOUNT=55200CFBE8ACFE7D; gg_info=1720252329; Hm_lpvt_36ae7161b950fe10c9fec864cb79c1d2=1720253191'
    }
    response = requests.get(url, headers=header_param, proxies=proxies)  # 发送HTTP GET请求
    soup = BeautifulSoup(response.text, 'html.parser')  # 解析HTML文档
    text_content=''
    videourl=''
    # 找到 class="entry-content" 的元素
    entry_content = soup.find(class_='entry-content')

    if entry_content:
        # 获取该元素下的第一个 <p> 元素
        first_p = entry_content.find('p')
        if first_p:
            # 提取第一个 <p> 元素的文本内容
            text_content = first_p.get_text()
            print(text_content.strip())  # 使用 strip() 去除文本前后的空白字符
        else:
            print("没有找到 <p> 元素")

        # 找到包含 data-video 的 div 标签
        player_div = soup.find('div', class_='b2-player')
        # 获取 data-video 的值
        video_data_str = player_div.get('data-video')
        # 解析 JSON 数据
        video_data = json.loads(video_data_str)
        # 获取视频 URL 并转换成正常访问地址
        video_url = video_data['url'].replace('\\/', '/')
        #video_tag=soup.find(class_="dplayer-video dplayer-video-current" , src=True)
        videourl=video_url
    else:
        print("没有找到 class='entry-content' 的元素")
    return  text_content,videourl
pathImg="D:/JAVA/UploadFile/xbgame/Images/"
pathVideo="D:/JAVA/UploadFile/xbgame/Videos/"
# 设置代理
proxies = {
    'http': '127.0.0.1:7890',
    'https': '127.0.0.1:7890',
}
#根据标题提取中英文名字
def extract_names(original_string):
    # 寻找书名号的位置
    start_index = original_string.find("《")
    end_index = original_string.find("》")

    # 提取书名号中的内容
    if start_index != -1 and end_index != -1:
        content = original_string[start_index + 1:end_index]
    else:
        return "", ""

    # 根据 '/' 分割字符串
    parts = content.split('/')

    # 提取 name1 和 name2
    if len(parts) >= 2:
        name1 = parts[0].strip()  # 去除首尾空格
        name2 = parts[1].strip()  # 去除首尾空格
    else:
        name1 = ""
        name2 = ""

    return name1, name2

#调用Main方法
requests_gamepostlist(6)
#get_game_introduce('https://www.xbgame.net/197441.html')
#contes,videoud=get_game_introduce('https://www.xbgame.net/197441.html')
#downimg.download_image(videoud,pathVideo+os.path.basename(videoud).split('.')[0]+'.mp4')

