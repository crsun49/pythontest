def readTxt():
    file_path = 'C:/Users/ODC/Desktop/33/11.txt'  # 文件路径
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()  # 逐行读取文件内容
            values = []  # 存储每一行的列表

            for line in lines:
                line = line.strip()  # 去除行首尾的空白字符
                values.append(line)  # 将每一行添加到列表中

            print(values)
    except FileNotFoundError:
        print(f"文件 '{file_path}' 不存在")
    except PermissionError:
        print(f"没有权限访问文件 '{file_path}'")
    except Exception as e:
        print(f"发生错误：{str(e)}")
def readUrlList():
    while True:
        with open("C:/Users/Administrator/Desktop/33/1.txt", "r+") as f:
            line = f.readline()
            if not line:
                break  # 遇到文件末尾，退出循环
            line = line.strip()  # 去除行尾的换行符和空白字符
            print(line)

            # 移动文件指针到下一行的开头
            f.seek(len(line) + len("\n"))
            content = f.read()
            f.seek(0)
            f.write(content.strip())  # 去除内容首尾的空白字符
            f.truncate()
            return line
