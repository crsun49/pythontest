import requests
from bs4 import BeautifulSoup
import re
import html
#抓取网站内容
def download_image(img_url, save_path):
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print('图片已保存到', save_path)
    else:
        print('请求失败，状态码为', response.status_code)
#去掉文件中不能包含的特殊自费
def sanitize_filename(filename):
    # 定义不允许出现的字符（这里以<>:"/\|?*为例）
    forbidden_chars = r'[<>:"/\\|?*]'
    # 使用空字符串替换非法字符
    sanitized_filename = re.sub(forbidden_chars, '', filename)
    return sanitized_filename
url = 'https://www.ahhhhfs.com'  # 指定网页的URL地址

try:
    response = requests.get(url)  # 发送HTTP GET请求
    soup = BeautifulSoup(response.text, 'html.parser')  # 解析HTML文档
    # 根据模块ID找到对应的<div>标签
    module_div = soup.find('div', class_='posts-warp row row-cols-1 row-cols-md-2 g-2 g-md-3 g-lg-4')
    module_col_div=module_div.find_all('div', class_='col')
    #pattern = r'class="media(.*?) data-bg="(.*?)"'  # 使用括号将需要提取的内容分组
    pattern = r'data-bg="(.*?)" href="(.*?)" (.*?) title="(.*?)"'
    title= r'title="(.*?)"'

    data_list = []
    for col in module_col_div:
        match = re.search(pattern, str(col))
        match2 = re.search(title, str(col))
        if match:
            img_url = match.group(1)
            url = match.group(2)
            title = match.group(4)
            download_image(img_url,"C:/Users/ODC/Desktop/33/"+sanitize_filename(title)+".jpg")
            data = {
                'img_url': img_url,
                'url': url,
                'title': title
            }
            data_list.append(data)
        else:
            print("未找到匹配的内容")
    print(data_list)
except requests.exceptions.RequestException as e:
    print(f"发生请求异常：{str(e)}")
except Exception as e:
    print(f"发生错误：{str(e)}")

