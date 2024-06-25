import os
import requests
from bs4 import BeautifulSoup
import ConSQL as conpipi
from datetime import datetime
import uuid
import time
import random
def scrape_page(url):
    # 发送HTTP请求并获取页面内容
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功

    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有符合条件的posts-item
    posts_items = soup.select('div.posts-row.ajaxpager > posts.posts-item.list.ajax-item.flex')




    # 初始化数组存储数据
    hrefs = []
    alts = []
    srcs = []
    context=[]

    for item in posts_items:
        # 查找<a>标签的href值
        a_tag = item.find('a', href=True)
        if a_tag:
            hrefs.append(a_tag['href'])
            context.append(fetch_and_process_content(a_tag['href']))

        # 查找<img>标签的alt值
        img_tag = item.find('img', alt=True, src=True)
        if img_tag:
            alts.append(img_tag['alt'])
            srcs.append(img_tag['data-src'])
        # # 生成一个0到3之间的随机整数
        # seconds = random.randint(0, 3)
        # print(f"暂停 {seconds} 秒")
        #
        # # 使用time.sleep()暂停指定的秒数
        # time.sleep(seconds)

    return hrefs, alts, srcs , context

def download_image(image_url, save_dir):
    # 获取图片名称
    image_name = os.path.basename(image_url)
    # 创建完整的文件路径
    image_path = os.path.join(save_dir, image_name)

    # 发送请求下载图片
    response = requests.get(image_url, stream=True)
    response.raise_for_status()  # 检查请求是否成功

    # 保存图片
    with open(image_path, 'wb') as file:
        for chunk in response.iter_content(8192):  # 分块写入
            file.write(chunk)
def fetch_and_process_content(url):
    try:
        # 发起请求并获取网页内容
        response = requests.get(url)
        html_content = response.text

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 找到所有 class="theme-box wp-posts-content" 的元素
        boxes = soup.find_all(class_="theme-box wp-posts-content")

        for box in boxes:
            # 找到第一个 <p> 标签
            first_p = box.find('p')

            # 如果第一个 <p> 标签存在且包含 <img> 元素，则移除其内容
            if first_p and first_p.find('img'):
                first_p.clear()
                first_p.decompose()
            unwanted_p = box.find(lambda tag: tag.name == 'p' and '加入VIP，可免费下载全站所有项目的拆解教' in tag.text)
            if unwanted_p:
                unwanted_p.decompose()

        # 返回处理后的 HTML
        processed_inner_html = ''.join(str(child) for child in box.children).strip()  # 去除首尾空白
        #processed_html = ''.join(str(child) for child in box.children)
        processed_inner_html = '\n'.join(line for line in processed_inner_html.splitlines() if line.strip())

        return processed_inner_html

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# 遍历多个分页URL
base_url = 'https://www.zhixing98.com/category/chuangyexiangmu/fuyeleimu/page/'
page_start = 1
page_end = 1  # 根据需要调整页数范围

all_hrefs = []
all_alts = []
all_srcs = []
all_filepaths=[]
all_context=[]
save_directory = "D:/images"  # 指定保存图片的目录
os.makedirs(save_directory, exist_ok=True)  # 确保目录存在

for page_num in range(page_start, page_end + 1):
    url = f"{base_url}{page_num}/"
    try:
        hrefs, alts, srcs , context = scrape_page(url)
        all_hrefs.extend(hrefs)
        all_alts.extend(alts)
        all_srcs.extend(srcs)
        all_context.extend(context)
    except requests.RequestException as e:
        print(f"Failed to scrape {url}: {e}")

# 下载所有图片
for src in all_srcs:
    try:
        download_image(src, save_directory)
        last_slash_index = src.rfind('/')

        # 截取最后一个斜杠之后的内容
        if last_slash_index != -1:  # 确保找到了斜杠
            #filename = url[last_slash_index + 1:]
            all_filepaths.append(src[last_slash_index + 1:])
            #print(filename)
        else:
            print("未找到斜杠")
        print(f"Downloaded: {src}")
    except requests.RequestException as e:
        print(f"Failed to download {src}: {e}")

#封装数据插入到数据库
data_to_insert =data_to_insert = [(uuid.uuid4(),first, last, email, 1,datetime.now(),filepath,context) for first, last, email,filepath ,context in zip(all_alts, all_hrefs, all_srcs,all_filepaths,all_context)]
db = con.SQLServerDB()
db.insert_data('p_zhixingfuye', ['id','title', 'src', 'img','status','createtime','filepath','context'], data_to_insert)
print("All Hrefs:", all_hrefs)
print("All Alts:", all_alts)
print("All Srcs:", all_srcs)