import requests

def fetch_url_content(url):
    try:
        proxies = {
            'http': '127.0.0.1:33210',
            'https': '127.0.0.1:33210'
        }
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch URL. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

# 要获取内容的网址
url = 'https://x.com/paul9886'

# 调用函数获取网页内容
content = fetch_url_content(url)

# 打印获取到的内容
if content:
    print(content)