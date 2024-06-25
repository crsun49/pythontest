import cv2

def imgConversion(sourceImgPath,targetImgPath):
    # 读取低分辨率图像
    #image_low_res = cv2.imread('C:/Users/ODC/Desktop/33/0.jpg')
    image_low_res = cv2.imread(sourceImgPath)
    # 显示低分辨率图像
    # cv2.imshow('Low Resolution Image', image_low_res)
    # cv2.waitKey(0)

    # 获取低分辨率图像的尺寸
    height, width = image_low_res.shape[:2]
    # 设定目标高分辨率图像的尺寸（这里将尺寸放大2倍）
    new_height = height * 3
    new_width = width * 3
    # 使用双线性插值对图像进行放大
    image_high_res = cv2.resize(image_low_res, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    # # 显示高分辨率图像
    # cv2.imshow('High Resolution Image', image_high_res)
    # cv2.waitKey(0)
    # 保存高分辨率图像
    cv2.imwrite(targetImgPath, image_high_res)

    # 关闭窗口
    cv2.destroyAllWindows()
    print("图片转换成功")
