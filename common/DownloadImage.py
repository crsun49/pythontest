import requests
import os
#下载图片到指定地址
def download_image(img_url, save_path):
    # header_param = {
    #  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding':'gzip, deflate, br, zstd',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Cache-Control':'max-age=0',
    # 'If-Modified-Since':'Thu, 11 Aug 2022 18:12:56 GMT',
    # 'If-None-Match':'856e337c1fb37d099ff8bfb9de85f226',
    # 'Priority':'u=0, i',
    # 'Sec-Ch-Ua':'Not/A)Brand;v=8,Chromium;v=126, Google Chrome;v=126',
    # 'Sec-Ch-Ua-Mobile':'?0',
    # 'Sec-Ch-Ua-Platform':'Windows',
    # 'Sec-Fetch-Dest':'document',
    # 'Sec-Fetch-Mode':'navigate',
    # 'Sec-Fetch-Site':'none',
    # 'Sec-Fetch-User':'?1',
    # 'Upgrade-Insecure-Requests':'1',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    # }
    # 确保目录存在，如果不存在则创建
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(img_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        f.close()

        print('图片已保存到', save_path)
    else:
        print('请求失败，状态码为', response.status_code)
    response.close()