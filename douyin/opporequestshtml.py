import requests
from bs4 import BeautifulSoup
import re
import time
import os
import html
#抓取网站内容
def download_image(img_url, save_path):
    header_param = {
        'authority': 'thebyrut.org',
        'method': 'POST',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': '_ga=GA1.1.995824374.1691507270; _ym_uid=1691507271355264713; _ym_d=1691507271; blconfirmed=yes; cf_clearance=tybur.a3BOI12U7.dt5krmiDDaAOX93hEBOZTm9vuQU-1693921138-0-1-8b271023.b9e29969.5a4ed549-0.2.1693921138; _ga_QX7E7T8PJ1=GS1.1.1693923114.21.1.1693923798.0.0.0',
        'Origin': 'https://thebyrut.org',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    response = requests.get(img_url,headers=header_param)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        f.close()

        print('图片已保存到', save_path)
    else:
        print('请求失败，状态码为', response.status_code)
    response.close()
#去掉文件中不能包含的特殊自费
def sanitize_filename(filename):
    # 定义不允许出现的字符（这里以<>:"/\|?*为例）
    forbidden_chars = r'[<>:"/\\|?*]'
    # 使用空字符串替换非法字符
    sanitized_filename = re.sub(forbidden_chars, '', filename)
    return sanitized_filename
def requests_post(url):
    # 定义不允许出现的字符（这里以<>:"/\|?*为例）
    header_param = {
        'authority': 'thebyrut.org',
        'method': 'POST',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Length': '128',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': '_ga=GA1.1.995824374.1691507270; _ym_uid=1691507271355264713; _ym_d=1691507271; blconfirmed=yes; cf_clearance=RgVk5B_iyd_XiRijZMIDNfvnmFxTilkFMeK9xvhghhc-1693745612-0-1-8b271023.b9e29969.5a4ed549-0.2.1693745612; _ym_isad=2; _ym_visorc=b; PHPSESSID=05ebc729690fd5799ba1f64bf1fa3e00; _ga_QX7E7T8PJ1=GS1.1.1693745609.18.1.1693746430.0.0.0',
        'Origin': 'https://thebyrut.org',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    response = requests.get(url, headers=header_param)  # 发送HTTP GET请求
    soup = BeautifulSoup(response.text, 'html.parser')  # 解析HTML文档
    return soup

def requests_gamepostlist(page):
    # 定义不允许出现的字符（这里以<>:"/\|?*为例）
    header_param = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Cookie': '_ga=GA1.1.1629325005.1693923322; _ym_uid=1694005782435888250; _ym_d=1694005782; PHPSESSID=0a680d4a765c452cfe02d099fe445e8d; _ga_QX7E7T8PJ1=GS1.1.1694613070.15.1.1694613084.0.0.0'
    }
    form_data = {
        'name':'top_main_all',
        'cstart':str(page),
        'action':'getpage'
    }

    response = requests.post('https://thebyrut.org/engine/mods/custom/ajax.php', headers=header_param,data=form_data)  # 发送HTTP GET请求
    soup = BeautifulSoup(response.text, 'html.parser')  # 解析HTML文档
    html = response.text
    #查找标题

    pattern = r'<a\s+href="([^"]+)">\s*<img[^>]+\salt="([^"]+)"'  # 使用括号将需要提取的内容分组

    matches = re.findall(pattern, html)
    srcarray = []
    altarray = []
    with open("C:/Users/Administrator/Desktop/33/1.txt", "w") as f:
        for match in matches:
            img_src = match[0]
            img_alt = match[1]
            line = f"{img_src}|{img_alt.replace('&#039;','').replace(':',' ')}\n"
            srcarray.append("'"+img_src+"'")
            altarray.append("'"+img_alt.replace('&#039;','').replace(':',' ')+"'")
        f.write( "[" + ", ".join(srcarray) + "]\n")
        f.write( "[" + ", ".join(altarray) + "]")
    print('地址书写完成')
    # # 打印匹配结果
    # for match in matches:
    #     link = match[0]
    #     alt = match[1]
    #     print("Link:", link)
    #     print("Alt Text:", alt)
    #     #print()


def requests_zwlist(page):
    # 定义不允许出现的字符（这里以<>:"/\|?*为例）
    header_param = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }
    form_data ={"prompt": "《Stardew Valley》告诉我这个游戏的中文名称，直接返回用《》括起来的就行，并且后面帮忙写20-30个字的游戏介绍",
            "userId": "#/chat/1694694080233",
            "network": "true",
            "system": "",
            "withoutContext": "false",
            "stream": "false"
        }
    response = requests.post('https://api.binjie.fun/api/generateStream?refer__1360=n4mx2DuDnDgA0%3DDkDcDGx059e1lEh03rD', headers=header_param,data=form_data)  # 发送HTTP GET请求
    soup = BeautifulSoup(response.text, 'html.parser')  # 解析HTML文档
    html = response.text
#查找标题

def main(url,fileName):
    #url = 'https://byrut.org/23887-starfield.html'  # 指定网页的URL地址
    # headers = {
    #     'authority': 'thebyrut.org',
    #     'method': 'GET',
    #     'scheme':'https',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    #     'path': '/2536-counter-strike-source.html',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #     'Accept-Language': 'zh-CN,zh;q=0.9',
    #     'Accept-Encoding':'gzip, deflate, br',
    #     'Cache-Control':'max-age=0',
    #     'Cookie':'_ga=GA1.1.1629325005.1693923322; _ym_uid=1694005782435888250; _ym_d=1694005782; PHPSESSID=80b5ac8c05cce01274f515bbf1044491; _ga_QX7E7T8PJ1=GS1.1.1694352541.10.0.1694352541.0.0.0; _ym_isad=2; _ym_visorc=b',
    #     'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    #     'Sec-Ch-Ua-Mobile': '0',
    #     'Sec-Fetch-Dest': 'document',
    #     'Sec-Ch-Ua-Platform': 'Windows',
    #     'Sec-Fetch-Site': 'none',
    #     'Sec-Fetch-User': '1',
    #      'Upgrade-Insecure-Requests': '1',
    #     'Sec-Fetch-Mode':'navigate'
    # }
    headers = {
        'method': 'GET',
        'scheme':'https',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Cookie':'_ga=GA1.1.1629325005.1693923322; _ym_uid=1694005782435888250; _ym_d=1694005782; PHPSESSID=80b5ac8c05cce01274f515bbf1044491; _ga_QX7E7T8PJ1=GS1.1.1694352541.10.0.1694352541.0.0.0; _ym_isad=2; _ym_visorc=b'
    }
    try:
        response = requests.get(url, headers=headers)  # 发送HTTP GET请求
        soup = BeautifulSoup(response.text, 'html.parser')  # 解析HTML文档
        html = response.text
        #查找标题
        # module_div = soup.find('div', class_='posts-warp row row-cols-1 row-cols-md-2 g-2 g-md-3 g-lg-4')
        # module_col_div=module_div.find_all('div', class_='col')
        #pattern = r'class="media(.*?) data-bg="(.*?)"'  # 使用括号将需要提取的内容分组
        #pattern = r'<h1>(.*?)</h1>'
        pattern = r'<div class="poster-imgbox">.*?<img src="(.*?)" class="(.*?)" alt="(.*?)">.*?<h1>(.*?)</h1>.*?type="video/webm">.*?<source src="(.*?)" type="video/mp4">'  # 使用括号将需要提取的内容分组
        match = re.search(pattern, html,re.DOTALL)
        title =''
        if match:
            img_url = match.group(1)
            title = sanitize_filename(match.group(4))
            vido_url = match.group(5).replace("microtrailer", "movie_max")
            if vido_url:
                download_image('https://thebyrut.org'+img_url , "C:/Users/Administrator/Desktop/33/"+fileName+".jpg")
                time.sleep(2)
                download_image(vido_url, "C:/Users/Administrator/Desktop/33/"+fileName+".mp4")
                size=get_file_size("C:/Users/Administrator/Desktop/33/"+fileName+".mp4")
                if size==0:
                    return '-1'
        return title
    except requests.exceptions.RequestException as e:
        print(f"发生请求异常：{str(e)}")
    except Exception as e:
        print(f"发生错误：{str(e)}")
def get_file_size(file_path):
    size = os.path.getsize(file_path)
    return size
#sid=get_file_size('C:/Users/Administrator/Desktop/33/21.mp4')
#main('https://thebyrut.org/484-mount-and-blade-warband.html','0')
#requests_gamepostlist(7)
#requests_zwlist(1)