import os
import shutil
from PIL import Image
def compare_images(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # 将图片转换为统一的尺寸
    size = (256, 256)
    image1 = image1.resize(size).convert("RGB")
    image2 = image2.resize(size).convert("RGB")

    # 计算两张图片的均方误差 (MSE)
    mse = 0
    for i in range(size[0]):
        for j in range(size[1]):
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))
            for k in range(3):
                mse += (pixel1[k] - pixel2[k]) ** 2
    mse /= size[0] * size[1]

    # 判断两张图片是否相同
    threshold = 30  # 阈值
    if mse <= threshold:
        return True
    else:
        return False
def transfer_images_from_phone(directory):
    # 获取手机指定目录下的前两张图片文件名
    cmd = f'adb shell "ls -p {directory} | grep -v / | head -n 2"'
    res = os.popen(cmd).read().strip()
    file_list = res.split("\n")

    if len(file_list) < 2:
        print("目录下图片数量不足。")
        return

    # 将图片从手机拷贝到电脑
    computer_directory = "C:/Users/Administrator/Desktop/33"  # 电脑上的目录

    for i in range(2):
        phone_path = os.path.join(directory, file_list[i])
        computer_path = os.path.join(computer_directory, file_list[i])
        cmd = f'adb pull {phone_path} "{computer_path}"'
        os.system(cmd)
    # 获取前两张图片的路径
    image1_path = os.path.join(computer_directory, file_list[0])
    image2_path = os.path.join(computer_directory, file_list[1])

    # 比较两张图片
    if compare_images(image1_path, image2_path):
        print("两张图片相同。")
        return True

    else:
        print("两张图片不同。")
        return False
#transfer_images_from_phone('/storage/emulated/0/DCIM/Pindd/goods/')