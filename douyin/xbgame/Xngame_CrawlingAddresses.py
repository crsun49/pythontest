#抓取对应网站的标题和图片、详细地址信息并且下载图片到指定位置
import requests
import common.DownloadImage as downimg
from bs4 import BeautifulSoup
import os
import json
import re
import douyin.opporequestshtml as a
class Game:
    def __init__(self, title, src, href, game_intro):
        self.title = title
        self.src = src
        self.href = href
        self.game_intro = game_intro

    def __str__(self):
        return f"标题: {self.title}\n图片地址: {self.src}\n详细地址: {self.href}\n游戏介绍: {self.game_intro}\n"

    def to_dict(self):
        return {
            'title': self.title,
            'src': self.src,
            'href': self.href,
            'game_intro': self.game_intro
        }
pathImg="D:/JAVA/UploadFile/xbgame/Images/"
pathVideo="D:/JAVA/UploadFile/xbgame/Videos/"
def requests_gamepostlist(page):
    # 定义不允许出现的字符（这里以<>:"/\|?*为例）
    header_param = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Cookie': 'darkStyle=1; Hm_lvt_36ae7161b950fe10c9fec864cb79c1d2=1720252327; HMACCOUNT=55200CFBE8ACFE7D; gg_info=1720252329; Hm_lpvt_36ae7161b950fe10c9fec864cb79c1d2=1720253191'
    }
    response = requests.get('https://www.xbgame.net/pcgame/pcgame-1/page/'+str(page), headers=header_param)  # 发送HTTP GET请求
    soup = BeautifulSoup(response.text, 'html.parser')  # 解析HTML文档

    # hrefs = []   #详细地址数组
    # titles = []  #标题数据组
    # srcs = []    #图片地址
    # game_ntroduce=[] #游戏介绍

    # 创建游戏对象列表
    games = []
    # 找到所有 class="post-list-item item-post-style-1" 的元素
    boxes = soup.find_all(class_="post-list-item item-post-style-1")
    for box in boxes:
        img_tag=box.find("img", class_="post-thumb" , alt=True, src=True)
        a_tag=box.find("a", class_="thumb-link", href=True)
        match = re.search(r'apps/(\d+)/', img_tag['src'].split('?')[0])
        filename=""
        if match:
            filename = match.group(1)  # 获取匹配到的数字部分
        gameintroduce,videourl=get_game_introduce(a_tag['href'].split('?')[0])
        game = Game(img_tag['alt'], img_tag['src'].split('?')[0], a_tag['href'].split('?')[0], gameintroduce)
        #下载图片到指定目录
        downimg.download_image(img_tag['src'].split('?')[0],pathImg+filename+'.jpg')

        match = re.search(r'apps/(\d+)/', img_tag['src'].split('?')[0])
        videofilename=""
        if match:
            videofilename = match.group(1)  # 获取匹配到的数字部分
        #下载视频到指定目录
        downimg.download_image(videourl,pathVideo+videofilename+'.mp4')
        games.append(game)

#获取游戏介绍文本
def get_game_introduce(url):
    # 定义不允许出现的字符（这里以<>:"/\|?*为例）
    header_param = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Cookie': 'darkStyle=1; Hm_lvt_36ae7161b950fe10c9fec864cb79c1d2=1720252327; HMACCOUNT=55200CFBE8ACFE7D; gg_info=1720252329; Hm_lpvt_36ae7161b950fe10c9fec864cb79c1d2=1720253191'
    }
    response = requests.get(url, headers=header_param)  # 发送HTTP GET请求
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

#调用Main方法
requests_gamepostlist(1)
#get_game_introduce('https://www.xbgame.net/197441.html')
#contes,videoud=get_game_introduce('https://www.xbgame.net/197441.html')
#downimg.download_image(videoud,pathVideo+os.path.basename(videoud).split('.')[0]+'.mp4')

