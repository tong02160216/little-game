from PIL import Image
import collections

# 打开图片
img = Image.open('F:/code/little_game/云.png')

# 获取所有像素
pixels = list(img.getdata())

# 统计颜色
colors = collections.Counter(pixels)

print('图片尺寸:', img.size)
print('图片模式:', img.mode)

print('\n最常见的20种颜色 (RGB):')
for color, count in colors.most_common(20):
    print(f'  RGB{color} - 出现 {count} 次')

# 背景色（蓝色）
background_blue = (73, 128, 247)

print(f'\n背景蓝色 RGB{background_blue} 出现次数:', colors[background_blue])

# 过滤掉背景色，只看云朵的颜色
print('\n云朵颜色（排除透明背景）:')
cloud_colors = {}
for color, count in colors.items():
    # PNG图片有4个通道 (R, G, B, A)
    if len(color) == 4:
        r, g, b, a = color
        # 只统计不透明的像素 (alpha > 0)
        if a > 0:
            cloud_colors[color] = count
    elif len(color) == 3:
        r, g, b = color
        # 排除蓝色背景（RGB值中蓝色分量远大于红绿）
        if not (b > 200 and b > r + 50 and b > g + 50):
            cloud_colors[color] = count

# 按出现次数排序
cloud_colors_sorted = sorted(cloud_colors.items(), key=lambda x: x[1], reverse=True)

print(f'\n云朵部分的颜色（共 {len(cloud_colors_sorted)} 种）:')
for i, (color, count) in enumerate(cloud_colors_sorted[:30]):  # 显示前30种
    percentage = (count / len(pixels)) * 100
    print(f'  {i+1}. RGBA{color} - 出现 {count} 次 ({percentage:.2f}%)')

# 分析云朵颜色的RGB范围
if cloud_colors_sorted:
    cloud_only = [c for c, _ in cloud_colors_sorted]
    r_values = [c[0] for c in cloud_only]
    g_values = [c[1] for c in cloud_only]
    b_values = [c[2] for c in cloud_only]
    if len(cloud_only[0]) == 4:
        a_values = [c[3] for c in cloud_only]
    
    print('\n云朵颜色的RGB范围:')
    print(f'  红色(R): {min(r_values)} - {max(r_values)}')
    print(f'  绿色(G): {min(g_values)} - {max(g_values)}')
    print(f'  蓝色(B): {min(b_values)} - {max(b_values)}')
    
    print('\n云朵颜色的平均RGB值:')
    avg_r = sum(r_values) / len(r_values)
    avg_g = sum(g_values) / len(g_values)
    avg_b = sum(b_values) / len(b_values)
    print(f'  平均RGB: ({int(avg_r)}, {int(avg_g)}, {int(avg_b)})')
