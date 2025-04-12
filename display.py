import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# 设置图片文件夹路径
folder_path = 'E:\\虚拟C盘\\新建文件夹 (3)'  # 替换为你的图片文件夹路径

# 获取文件夹中所有图片的文件名
images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 检查是否有20张图片
if len(images) >= 20:
    # 创建一个5x4的子图网格
    fig, axes = plt.subplots(4, 5, figsize=(15, 12))

    # 遍历子图并展示图片
    for i, ax in enumerate(axes.flat):
        img_path = os.path.join(folder_path, images[i])
        img = mpimg.imread(img_path)
        ax.imshow(img)
        ax.axis('off')  # 不显示坐标轴

    # 调整子图之间的间距
    plt.tight_layout()
    plt.show()
else:
    print("图片数量不足20张，请确保文件夹中有至少20张图片。")