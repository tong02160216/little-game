from PIL import Image

# 加载气球图像
image_path = "F:/code/little_game/B1.png"  # 使用已存在的气球文件
output_path = "F:/code/little_game/B1_modified.png"
image = Image.open(image_path).convert("RGBA")

# 获取像素数据
pixels = image.load()
width, height = image.size

# 定义新的气球颜色
new_color = (0, 0, 255)  # 绿色

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # 保留高光（假设高光为接近白色的区域）
        if not (r > 200 and g > 200 and b > 200):
            # 修改非高光区域的颜色
            pixels[x, y] = (*new_color, a)

# 保存修改后的图像
image.save(output_path)
print(f"修改后的气球图像已保存到 {output_path}")