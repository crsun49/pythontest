import subprocess
import uiautomator2 as u2
import os

# 连接到设备
d = u2.connect_usb('498f62e8')
print(d.info)

# # 电脑上源文件路径和手机上目标路径
source_file_path = "C:/Users/ODC/Desktop/33/900+知乎赚钱案例大合集.jpg"
#target_directory = "/sdcard/1/"
target_directory = "/sdcard/DCIM/Camera/"

source_directory = "C:/Users/ODC/Desktop/33"
# 获取目录中的所有 JPG 文件
jpg_files = [file for file in os.listdir(source_directory) if file.lower().endswith(".jpg")]

# 遍历 JPG 文件并推送到手机上
i=0
for jpg_file in jpg_files:
    source_file_path = os.path.join(source_directory, jpg_file)
    d.push(source_file_path, target_directory)

#推送成功后刷新相册列表
d.shell("am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/")
print("文件推送成功")
#
# # 使用push方法将文件推送到设备
# d.push(source_file_path, target_directory)
##删除指定目录文件
#d.shell(f"rm /sdcard/1/61、Hrot.mp4")
# 使用 adb_shell 方法在设备上执行 rm 命令，删除目录中的所有 JPG 文件
#d.shell(f"rm {target_directory}/*.jpg")
#
# # 列出目标目录中的文件
# files = d.shell(f"ls {target_directory}")
# print(files)

# 验证文件是否成功推送
# if source_file_path.split("/")[-1] in files:
#     print("文件推送成功")
# else:
#     print("文件推送失败")