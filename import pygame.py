import pygame
import sys
import random
import turtle
import time
import math

# 初始化
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 圆点属性
x, y = WIDTH // 2, HEIGHT // 2
radius = 10
speed = 5

clock = pygame.time.Clock()

# 迷宫参数设置
CELL_SIZE = 30  # 每个单元格大小
MAZE_WIDTH = 21  # 迷宫宽度（建议为奇数）
MAZE_HEIGHT = 15  # 迷宫高度（建议为奇数）
SCREEN_WIDTH = CELL_SIZE * MAZE_WIDTH
SCREEN_HEIGHT = CELL_SIZE * MAZE_HEIGHT

# 颜色定义
BACKGROUND = (255, 255, 255)  # 白色背景（路径）
WALL = (255, 255, 255)        # 白色墙线
ARROW = (0, 0, 0)             # 起点黑色箭头

# 加载玩家图片
PLAYER_IMAGE = pygame.image.load("F:/code/little_game/023-snails.png")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))  # 调整玩家图片大小

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Little Snail Goes Home")

# 确保随机数生成器每次运行时生成不同的随机序列
random.seed()

def generate_maze(width, height):
    """使用深度优先算法生成随机迷宫"""
    # 初始化迷宫：1为墙，0为通路
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    # 起点设置在左上角(1,1)
    start_x, start_y = 1, 1
    maze[start_y][start_x] = 0
    
    # 栈用于深度优先搜索
    stack = [(start_x, start_y)]
    
    # 方向：右、左、下、上
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    
    while stack:
        x, y = stack[-1]
        neighbors = []
        
        # 检查所有可能的邻居
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and maze[ny][nx] == 1:
                neighbors.append((nx, ny))
        
        if neighbors:
            # 随机选择一个邻居
            nx, ny = random.choice(neighbors)
            # 将当前单元格与邻居之间的墙打通
            maze[(y + ny) // 2][(x + nx) // 2] = 0
            # 标记邻居为通路
            maze[ny][nx] = 0
            # 将邻居加入栈
            stack.append((nx, ny))
        else:
            # 回溯
            stack.pop()
    
    # 在迷宫生成函数中返回终点位置
    end_x, end_y = width - 2, height - 2  # 假设终点在右下角

    # 确保迷宫的终点在通路上
    while maze[end_y][end_x] == 1:  # 如果终点是墙，向左或向上调整
        if end_x > 1:
            end_x -= 1
        elif end_y > 1:
            end_y -= 1

    # 确保终点在通路上，搜索最近的通路
    if maze[end_y][end_x] == 1:
        queue = [(end_x, end_y)]
        visited = set(queue)
        while queue:
            x, y = queue.pop(0)
            if maze[y][x] == 0:  # 找到通路
                end_x, end_y = x, y
                break
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))

    return maze, (start_x, start_y), (end_x, end_y)

def draw_maze(maze, start, background_img=None):
    """绘制迷宫"""
    # 先用白色填充整个背景（路径颜色）
    screen.fill(BACKGROUND)
    
    # 使用固定的随机种子来确保每次绘制相同的像素纹理
    random.seed(42)
    
    # 先绘制路径的像素风格纹理
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 0:  # 路径
                # 在路径上添加像素风格的浅灰色点缀
                pixel_size = CELL_SIZE // 4
                for py in range(4):
                    for px in range(4):
                        # 50%概率添加浅灰色像素点（增加密度）
                        if random.random() < 0.5:
                            # 使用更深的灰色调
                            gray_value = random.randint(200, 230)
                            color = (gray_value, gray_value, gray_value)
                            pixel_rect = pygame.Rect(
                                x * CELL_SIZE + px * pixel_size,
                                y * CELL_SIZE + py * pixel_size,
                                pixel_size,
                                pixel_size
                            )
                            pygame.draw.rect(screen, color, pixel_rect)
    
    # 重置随机种子用于灌木丛
    random.seed(42)
    
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                # 如果有背景图，先绘制对应位置的背景图部分
                if background_img is not None:
                    # 从背景图裁剪出对应墙壁位置的部分
                    source_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    screen.blit(background_img, (x * CELL_SIZE, y * CELL_SIZE), source_rect)
                else:
                    # 没有背景图时，绘制白色墙壁
                    rect = pygame.Rect(
                        x * CELL_SIZE, 
                        y * CELL_SIZE, 
                        CELL_SIZE, 
                        CELL_SIZE
                    )
                    pygame.draw.rect(screen, WALL, rect)
                
                # 决定是否在这个墙格子上生成灌木丛（50%概率，增加密度）
                if random.random() < 0.5:
                    # 随机选择灌木丛大小（2x2、3x3 或 4x4 像素块，增加大尺寸）
                    bush_size = random.choice([2, 3, 3, 4])  # 3出现两次增加概率
                    pixel_size = CELL_SIZE // 4
                    
                    # 随机选择灌木丛位置（确保不会超出格子边界）
                    max_offset = 4 - bush_size
                    start_px = random.randint(0, max_offset) if max_offset > 0 else 0
                    start_py = random.randint(0, max_offset) if max_offset > 0 else 0
                    
                    # 选择这一丛灌木的基础绿色
                    green_shades = [
                        (34, 139, 34),   # 森林绿
                        (0, 128, 0),     # 纯绿
                        (50, 205, 50),   # 亮绿
                        (0, 100, 0),     # 深绿
                        (46, 139, 87)    # 海洋绿
                    ]
                    base_color = random.choice(green_shades)
                    
                    # 绘制一丛灌木
                    for py in range(bush_size):
                        for px in range(bush_size):
                            # 提高显示概率到90%，让灌木更密集
                            if random.random() < 0.9:
                                # 在基础颜色上添加一些随机变化（减少变化范围，让颜色更统一）
                                r = max(0, min(255, base_color[0] + random.randint(-15, 15)))
                                g = max(0, min(255, base_color[1] + random.randint(-15, 15)))
                                b = max(0, min(255, base_color[2] + random.randint(-8, 8)))
                                color = (r, g, b)
                                
                                actual_x = start_px + px
                                actual_y = start_py + py
                                # 确保不超出格子边界
                                if actual_x < 4 and actual_y < 4:
                                    pixel_rect = pygame.Rect(
                                        x * CELL_SIZE + actual_x * pixel_size,
                                        y * CELL_SIZE + actual_y * pixel_size,
                                        pixel_size,
                                        pixel_size
                                    )
                                    pygame.draw.rect(screen, color, pixel_rect)
    
    # 恢复随机数生成器
    random.seed()

# 生成静态像素块背景
def generate_static_pixel_background(width, height, block_size):
    background = []
    for i in range(0, height, block_size):
        row = []
        for j in range(0, width, block_size):
            color = (
                random.randint(0, 255),  # 随机红色分量
                random.randint(0, 255),  # 随机绿色分量
                random.randint(0, 255)   # 随机蓝色分量
            )
            row.append((j, i, block_size, block_size, color))
        background.append(row)
    return background

def draw_static_pixel_background(surface, background):
    for row in background:
        for block in row:
            x, y, block_width, block_height, color = block
            pygame.draw.rect(surface, color, (x, y, block_width, block_height))


# 添加结算画面的函数，使用气球图像
def show_congratulations_screen():
    # 加载背景图像作为气球背景
    background_image = pygame.image.load("F:/code/little_game/生成气球图片.png")

    # 在结算画面中绘制背景气球动画
    while True:  # 无限循环，保持画面
        screen.fill((255, 255, 255))  # 白色背景

        # 绘制背景气球
        # 绘制文字
        font = pygame.font.Font(None, 74)
        text = font.render("Congratulations!!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

        # 检测退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# 加载多个气球背景图像（使用convert_alpha保留透明通道）
balloon_images = []
balloon_files = [
    "F:/code/little_game/B1.png",
    "F:/code/little_game/B2.png",
    "F:/code/little_game/B4.png",
    "F:/code/little_game/B6.png"
]

# 加载所有气球图片（添加像素效果）
for file_path in balloon_files:
    img = pygame.image.load(file_path).convert_alpha()
    # 先缩小到原来的1/3，再放大回原尺寸，创建像素风格效果
    original_width = img.get_width()
    original_height = img.get_height()
    small_width = original_width // 3
    small_height = original_height // 3
    img = pygame.transform.scale(img, (small_width, small_height))
    img = pygame.transform.scale(img, (original_width, original_height))
    balloon_images.append(img)

# 定义气球类
class Balloon:
    def __init__(self):
        # 随机大小（控制远近，小的看起来远）
        self.scale = random.uniform(0.5, 1.5)  # 随机缩放比例
        self.image = random.choice(balloon_images)  # 随机选择气球图像
        # 缩放时添加像素效果（先缩小再放大）
        target_width = int(self.image.get_width() * self.scale)
        target_height = int(self.image.get_height() * self.scale)
        small_width = target_width // 3
        small_height = target_height // 3
        if small_width > 0 and small_height > 0:
            temp_image = pygame.transform.scale(self.image, (small_width, small_height))
            self.image = pygame.transform.scale(temp_image, (target_width, target_height))
        else:
            self.image = pygame.transform.scale(self.image, (target_width, target_height))

        # 随机位置（从四周开始）
        self.x = random.randint(-self.image.get_width(), SCREEN_WIDTH)
        self.y = random.randint(-self.image.get_height(), SCREEN_HEIGHT)

        # 速度设置（随机方向和速度）
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)

    def update(self):
        # 更新位置
        self.x += self.dx
        self.y += self.dy

        # 如果气球飞出屏幕，重置到随机位置
        if self.x < -self.image.get_width() or self.x > SCREEN_WIDTH or self.y < -self.image.get_height() or self.y > SCREEN_HEIGHT:
            self.__init__()

    def draw(self, surface):
        # 绘制气球
        surface.blit(self.image, (self.x, self.y))

# 创建气球列表
balloons = [Balloon() for _ in range(40)]  # 40个气球

# 确保字体初始化在主循环之前完成
pygame.font.init()
font = pygame.font.SysFont(["SimHei", "WenQuanYi Micro Hei", "Heiti TC"], 30)

# 定义 main 函数

def main():
    # 初始化 Pygame
    pygame.init()
    pygame.mixer.init()  # 初始化音频系统

    # 设置屏幕大小
    global SCREEN_WIDTH, SCREEN_HEIGHT, screen, clock
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # 设置迷宫参数
    global MAZE_WIDTH, MAZE_HEIGHT, CELL_SIZE, PLAYER_IMAGE
    MAZE_WIDTH, MAZE_HEIGHT = 20, 15
    CELL_SIZE = SCREEN_WIDTH // MAZE_WIDTH

    # 加载玩家图像
    PLAYER_IMAGE = pygame.image.load("F:/code/little_game/023-snails.png")
    PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))

    # 恢复蜗牛的大小
    PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))

    # 将蜗牛图片从中心等比放大三倍
    PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE * 3, CELL_SIZE * 3))

    # 确保房子图片为全局变量
    global HOUSE_IMAGE
    HOUSE_IMAGE = pygame.image.load("F:/code/little_game/房子3.png")
    HOUSE_IMAGE = pygame.transform.scale(HOUSE_IMAGE, (CELL_SIZE * 2, CELL_SIZE * 2))  # 调整房子大小
    HOUSE_IMAGE = pygame.transform.scale(HOUSE_IMAGE, (CELL_SIZE // 2, CELL_SIZE // 2))  # 缩小
    HOUSE_IMAGE = pygame.transform.scale(HOUSE_IMAGE, (CELL_SIZE * 2, CELL_SIZE * 2))  # 放大回原尺寸

    # 加载背景图
    try:
        background_image = pygame.image.load("F:/code/little_game/生成草地背景图.png")
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        print("成功加载背景图")
    except:
        background_image = None
        print("背景图加载失败，将使用纯色背景")

    # 加载白菜图片
    try:
        global CABBAGE_IMAGE
        CABBAGE_IMAGE = pygame.image.load("F:/code/little_game/新鲜果蔬_新鲜蔬菜包菜.png")
        # 先缩小再放大，创建像素风格效果
        small_size = CELL_SIZE // 2
        CABBAGE_IMAGE = pygame.transform.scale(CABBAGE_IMAGE, (small_size, small_size))
        CABBAGE_IMAGE = pygame.transform.scale(CABBAGE_IMAGE, (CELL_SIZE, CELL_SIZE))
        print("成功加载白菜图片（像素风格）")
    except:
        CABBAGE_IMAGE = None
        print("白菜图片加载失败")

    # 加载苹果图片
    try:
        global APPLE_IMAGE
        APPLE_IMAGE = pygame.image.load("F:/code/little_game/苹果.png")
        # 先缩小再放大，创建像素风格效果
        small_size = CELL_SIZE // 2
        APPLE_IMAGE = pygame.transform.scale(APPLE_IMAGE, (small_size, small_size))
        APPLE_IMAGE = pygame.transform.scale(APPLE_IMAGE, (CELL_SIZE, CELL_SIZE))
        print("成功加载苹果图片（像素风格）")
    except:
        APPLE_IMAGE = None
        print("苹果图片加载失败")

    # 加载香蕉图片
    try:
        global BANANA_IMAGE
        BANANA_IMAGE = pygame.image.load("F:/code/little_game/香蕉.png")
        # 先缩小再放大，创建像素风格效果
        small_size = CELL_SIZE // 2
        BANANA_IMAGE = pygame.transform.scale(BANANA_IMAGE, (small_size, small_size))
        BANANA_IMAGE = pygame.transform.scale(BANANA_IMAGE, (CELL_SIZE, CELL_SIZE))
        print("成功加载香蕉图片（像素风格）")
    except:
        BANANA_IMAGE = None
        print("香蕉图片加载失败")

    # 生成迷宫
    maze, start, end = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)  # 获取终点位置
    player_x, player_y = start
    end_x, end_y = end

    # 定义生成食物的函数
    def generate_food_items():
        """随机生成白菜、苹果和香蕉的位置，尽量分散在地图各处"""
        new_cabbages = []
        new_apples = []
        new_bananas = []
        
        # 获取所有可用路径位置
        path_cells = []
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                if maze[y][x] == 0 and (x, y) != start and (x, y) != end:
                    path_cells.append((x, y))
        
        if len(path_cells) >= 6:
            # 将地图分成四个区域，让食物分散分布
            # 左上、右上、左下、右下四个区域
            mid_x = MAZE_WIDTH // 2
            mid_y = MAZE_HEIGHT // 2
            
            # 分别获取四个区域的路径点
            top_left = [(x, y) for x, y in path_cells if x < mid_x and y < mid_y]
            top_right = [(x, y) for x, y in path_cells if x >= mid_x and y < mid_y]
            bottom_left = [(x, y) for x, y in path_cells if x < mid_x and y >= mid_y]
            bottom_right = [(x, y) for x, y in path_cells if x >= mid_x and y >= mid_y]
            
            selected_positions = []
            regions = [top_left, top_right, bottom_left, bottom_right]
            
            # 从每个区域尝试随机选择食物位置
            for region in regions:
                if region:
                    # 从该区域随机选择1-2个位置
                    num_items = min(2, len(region))
                    selected_positions.extend(random.sample(region, num_items))
            
            # 如果选中的位置不够6个，从所有路径中补充
            if len(selected_positions) < 6:
                remaining = [pos for pos in path_cells if pos not in selected_positions]
                needed = 6 - len(selected_positions)
                if len(remaining) >= needed:
                    selected_positions.extend(random.sample(remaining, needed))
            
            # 随机打乱顺序
            random.shuffle(selected_positions)
            
            # 分配给不同类型的食物
            if len(selected_positions) >= 6:
                if CABBAGE_IMAGE is not None:
                    new_cabbages = selected_positions[:2]  # 前两个给白菜
                    print(f"白菜位置: {new_cabbages}")
                if APPLE_IMAGE is not None:
                    new_apples = selected_positions[2:4]  # 中间两个给苹果
                    print(f"苹果位置: {new_apples}")
                if BANANA_IMAGE is not None:
                    new_bananas = selected_positions[4:6]  # 后两个给香蕉
                    print(f"香蕉位置: {new_bananas}")
        
        return new_cabbages, new_apples, new_bananas

    # 初始生成食物
    cabbages, apples, bananas = generate_food_items()

    # 初始化分数
    score = 0
    
    # 分数动画相关变量
    score_scale = 1.0  # 分数文字缩放比例
    score_animating = False  # 是否正在播放动画
    score_animation_frame = 0  # 动画帧计数
    
    # 分数颜色变化
    def get_score_color(score):
        """根据分数返回对应的颜色，从白色逐渐变为深红色"""
        if score == 0:
            return (255, 255, 255)  # 白色
        elif score == 1:
            return (255, 200, 200)  # 浅粉色
        elif score == 2:
            return (255, 150, 150)  # 粉红色
        elif score == 3:
            return (255, 100, 100)  # 浅红色
        elif score == 4:
            return (255, 50, 50)    # 红色
        else:  # score >= 5
            return (200, 0, 0)      # 深红色

    # 定义庆祝气球类
    class CelebrationBalloon:
        def __init__(self, balloon_img=None):
            # 如果指定了气球图片，使用指定的，否则随机选择
            if balloon_img is not None:
                self.image = balloon_img
            else:
                self.image = random.choice(balloon_images)
            # 随机大小（缩小差异范围，从0.6到1.0）
            self.scale = random.uniform(0.6, 1.0)
            # 缩放时保持像素效果（先缩小再放大）
            target_width = int(self.image.get_width() * self.scale)
            target_height = int(self.image.get_height() * self.scale)
            small_width = target_width // 3
            small_height = target_height // 3
            if small_width > 0 and small_height > 0:
                temp_image = pygame.transform.scale(self.image, (small_width, small_height))
                self.image = pygame.transform.scale(temp_image, (target_width, target_height))
            else:
                self.image = pygame.transform.scale(self.image, (target_width, target_height))
            # 随机X位置
            self.x = random.randint(0, SCREEN_WIDTH - self.image.get_width())
            # 从屏幕下方开始
            self.y = SCREEN_HEIGHT + random.randint(0, 200)
            # 上升速度（随机）
            self.speed = random.uniform(3, 6)
            # 左右摆动
            self.swing_offset = random.uniform(-1, 1)
            self.swing_speed = random.uniform(0.02, 0.05)
            self.swing_angle = random.uniform(0, 3.14 * 2)
        
        def update(self):
            # 向上移动
            self.y -= self.speed
            # 左右摆动
            self.swing_angle += self.swing_speed
            # 如果飞出屏幕顶部，重置到底部
            if self.y < -self.image.get_height():
                self.__init__()
        
        def draw(self, surface):
            # 计算摆动后的X位置
            swing_x = self.x + math.sin(self.swing_angle) * 20 * self.scale
            surface.blit(self.image, (swing_x, self.y))
    
    # 创建庆祝气球列表（初始为空，胜利时才创建）
    celebration_balloons = []
    
    # 云朵动画相关变量
    cloud_float_offset = 0  # 云朵上下浮动偏移量
    cloud_float_speed = 0.05  # 云朵浮动速度
    cloud_float_angle = 0  # 云朵浮动角度

    # 用于跟踪是否已经播放庆祝音效
    celebration_played = False
    applause_played = False
    celebration_started = False  # 用于锁定庆祝状态，确保庆祝画面持续显示
    
    # 尝试加载庆祝音效（支持 WAV 或 MP3 格式）
    try:
        celebration_sound = pygame.mixer.Sound("F:/code/little_game/celebration.mp3")
        celebration_sound.set_volume(1.0)  # 设置庆祝音效音量为100%（最大）
        sound_loaded = True
        print("成功加载庆祝音效（MP3格式）")
    except:
        try:
            celebration_sound = pygame.mixer.Sound("F:/code/little_game/celebration.wav")
            celebration_sound.set_volume(1.0)
            sound_loaded = True
            print("成功加载庆祝音效（WAV格式）")
        except:
            print("庆祝音效文件未找到（celebration.mp3 或 celebration.wav），游戏将正常运行但没有音效")
            sound_loaded = False
    
    # 尝试加载欢呼声音效
    try:
        applause_sound = pygame.mixer.Sound("F:/code/little_game/applause-cheer-236786.mp3")
        applause_sound.set_volume(0.8)  # 设置欢呼声音量为80%
        applause_loaded = True
        print("成功加载欢呼声音效")
    except:
        print("欢呼声音效文件未找到，游戏将正常运行但没有欢呼声")
        applause_loaded = False
    
    # 尝试加载吃白菜音效
    try:
        cabbage_sound = pygame.mixer.Sound("F:/code/little_game/shine-11-268907.mp3")
        cabbage_sound.set_volume(0.6)  # 设置吃白菜音效音量为60%
        cabbage_sound_loaded = True
        print("成功加载吃白菜音效")
    except:
        print("吃白菜音效文件未找到，游戏将正常运行但没有吃白菜音效")
        cabbage_sound_loaded = False
    
    # 吃苹果使用同样的音效
    apple_sound_loaded = cabbage_sound_loaded
    if apple_sound_loaded:
        apple_sound = cabbage_sound  # 使用相同的音效
    
    # 加载并播放背景音乐
    try:
        pygame.mixer.music.load("F:/code/little_game/10月22日.WAV")
        pygame.mixer.music.set_volume(0.3)  # 设置背景音乐音量为30%
        pygame.mixer.music.play(-1)  # -1 表示循环播放
        print("成功加载并播放背景音乐")
    except:
        print("背景音乐文件未找到，游戏将正常运行但没有背景音乐")

    # 主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    maze, start, end = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
                    player_x, player_y = start
                    end_x, end_y = end
                    celebration_played = False  # 重置音效标志
                    applause_played = False  # 重置欢呼声标志
                    # 重新生成食物
                    cabbages, apples, bananas = generate_food_items()
                    # 重置分数
                    score = 0
                    # 重新播放背景音乐
                    try:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.play(-1)
                    except:
                        pass

        # 获取按键状态
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and maze[player_y - 1][player_x] == 0:
            player_y -= 1
        if keys[pygame.K_s] and maze[player_y + 1][player_x] == 0:
            player_y += 1
        if keys[pygame.K_a] and maze[player_y][player_x - 1] == 0:
            player_x -= 1
        if keys[pygame.K_d] and maze[player_y][player_x + 1] == 0:
            player_x += 1

        # 检查蜗牛是否碰到白菜（遍历所有白菜）
        for cabbage in cabbages[:]:  # 使用切片创建副本以便在循环中修改列表
            cabbage_x, cabbage_y = cabbage
            if player_x == cabbage_x and player_y == cabbage_y:
                # 白菜被吃掉，从列表中移除
                cabbages.remove(cabbage)
                # 增加分数
                score += 1
                # 触发分数动画
                score_animating = True
                score_animation_frame = 0
                # 播放吃白菜音效
                if cabbage_sound_loaded:
                    cabbage_sound.play()
                print(f"蜗牛吃掉了白菜！位置: ({cabbage_x}, {cabbage_y})，当前分数: {score}")

        # 检查蜗牛是否碰到苹果（遍历所有苹果）
        for apple in apples[:]:  # 使用切片创建副本以便在循环中修改列表
            apple_x, apple_y = apple
            if player_x == apple_x and player_y == apple_y:
                # 苹果被吃掉，从列表中移除
                apples.remove(apple)
                # 增加分数
                score += 1
                # 触发分数动画
                score_animating = True
                score_animation_frame = 0
                # 播放吃苹果音效
                if apple_sound_loaded:
                    apple_sound.play()
                print(f"蜗牛吃掉了苹果！位置: ({apple_x}, {apple_y})，当前分数: {score}")

        # 检查蜗牛是否碰到香蕉（遍历所有香蕉）
        for banana in bananas[:]:  # 使用切片创建副本以便在循环中修改列表
            banana_x, banana_y = banana
            if player_x == banana_x and player_y == banana_y:
                # 香蕉被吃掉，从列表中移除
                bananas.remove(banana)
                # 增加分数
                score += 1
                # 触发分数动画
                score_animating = True
                score_animation_frame = 0
                # 播放吃香蕉音效（使用相同音效）
                if apple_sound_loaded:
                    apple_sound.play()
                print(f"蜗牛吃掉了香蕉！位置: ({banana_x}, {banana_y})，当前分数: {score}")

        # 检查是否到达房子（庆祝画面）
        # 房子的位置偏移（在这里定义，无论是否庆祝都可用）
        house_offset_x, house_offset_y = -CELL_SIZE // 2, -CELL_SIZE + CELL_SIZE // 4
        
        # 无论是否庆祝，都绘制迷宫和游戏元素
        draw_maze(maze, start, background_image)
        
        # 绘制所有白菜
        if CABBAGE_IMAGE is not None:
            for cabbage_x, cabbage_y in cabbages:
                # 白菜居中绘制（现在是1倍CELL_SIZE，不需要偏移）
                screen.blit(CABBAGE_IMAGE, (cabbage_x * CELL_SIZE, cabbage_y * CELL_SIZE))

        # 绘制所有苹果
        if APPLE_IMAGE is not None:
            for apple_x, apple_y in apples:
                # 苹果居中绘制（现在是1倍CELL_SIZE，不需要偏移）
                screen.blit(APPLE_IMAGE, (apple_x * CELL_SIZE, apple_y * CELL_SIZE))

        # 绘制所有香蕉
        if BANANA_IMAGE is not None:
            for banana_x, banana_y in bananas:
                # 香蕉居中绘制（现在是1倍CELL_SIZE，不需要偏移）
                screen.blit(BANANA_IMAGE, (banana_x * CELL_SIZE, banana_y * CELL_SIZE))

        # 调整蜗牛的位置，使其居中于迷宫单元格
        snail_offset_x = (CELL_SIZE * 3 - CELL_SIZE) // 2
        snail_offset_y = (CELL_SIZE * 3 - CELL_SIZE) // 2
        screen.blit(PLAYER_IMAGE, (player_x * CELL_SIZE - snail_offset_x, player_y * CELL_SIZE - snail_offset_y))

        # 绘制房子
        screen.blit(HOUSE_IMAGE, ((end_x * CELL_SIZE) + house_offset_x, (end_y * CELL_SIZE) + house_offset_y))
        
        # 检查是否到达房子，启动庆祝
        if player_x == end_x and player_y == end_y and not celebration_started:
            celebration_started = True  # 锁定庆祝状态
        
        # 如果庆祝已经开始，持续显示庆祝画面
        if celebration_started:
            # 播放庆祝音效（只播放一次）
            if not celebration_played:
                # 停止背景音乐
                pygame.mixer.music.stop()
                # 播放庆祝音效
                if sound_loaded:
                    celebration_sound.play()
                # 立即播放欢呼声
                if applause_loaded:
                    applause_sound.play()
                celebration_played = True
                applause_played = True
                # 创建庆祝气球（28个，每种气球7个，平均分配）
                celebration_balloons = []
                balloons_per_type = 7  # 每种气球7个
                for balloon_img in balloon_images:
                    for _ in range(balloons_per_type):
                        celebration_balloons.append(CelebrationBalloon(balloon_img))
                # 打乱顺序让气球更随机
                random.shuffle(celebration_balloons)
            
            # 更新并绘制庆祝气球
            for balloon in celebration_balloons:
                balloon.update()
                balloon.draw(screen)
            
            # 更新云朵浮动动画
            cloud_float_angle += cloud_float_speed
            cloud_float_offset = math.sin(cloud_float_angle) * 15  # 上下浮动15像素
            
            # 绘制云朵图片（像素风格，基于云.png形状）
            try:
                cloud_img = pygame.image.load("F:/code/little_game/云.png").convert_alpha()
                
                # 设置云朵大小以包裹文字
                # "Congratulations!!" 文字大约500-550像素宽，云朵设置为800像素确保完全包裹
                cloud_width = 800
                cloud_height = int(cloud_img.get_height() * (cloud_width / cloud_img.get_width()))
                
                # 先缩小到1/8大小，再放大回目标尺寸，创建明显的像素风格效果
                small_width = cloud_width // 8
                small_height = cloud_height // 8
                if small_width > 0 and small_height > 0:
                    cloud_img_small = pygame.transform.scale(cloud_img, (small_width, small_height))
                    cloud_img_scaled = pygame.transform.scale(cloud_img_small, (cloud_width, cloud_height))
                else:
                    cloud_img_scaled = pygame.transform.scale(cloud_img, (cloud_width, cloud_height))
                
                # 将云朵居中绘制在文字后面，添加上下浮动效果
                cloud_x = SCREEN_WIDTH // 2 - cloud_width // 2
                cloud_y = SCREEN_HEIGHT // 2 - cloud_height // 2 - 50 + cloud_float_offset  # 向上移动50像素 + 浮动偏移
                screen.blit(cloud_img_scaled, (cloud_x, cloud_y))
            except Exception as e:
                print(f"云朵图片加载失败: {e}")
            
            # 使用可爱的字体显示祝贺信息（像素风格）
            # 使用方方正正的等宽字体
            square_fonts = ["Courier New", "Consolas", "Monaco", "Lucida Console", "DejaVu Sans Mono"]
            congrats_font = None
            for font_name in square_fonts:
                try:
                    congrats_font = pygame.font.SysFont(font_name, 74, bold=True)
                    break
                except:
                    continue
            
            # 如果找不到方正字体，使用默认字体
            if congrats_font is None:
                congrats_font = pygame.font.Font(None, 74)
            
            # 先渲染小尺寸文字，再放大创建像素风格（更小的字体，更大的像素块）
            small_font = pygame.font.SysFont(square_fonts[0] if congrats_font else None, 16, bold=True)
            small_text = small_font.render("Congratulations!!", True, (255, 100, 150))  # 粉红色更可爱
            
            # 获取小文字的尺寸
            small_width = small_text.get_width()
            small_height = small_text.get_height()
            
            # 放大4.5倍创建更大的像素效果
            pixel_text = pygame.transform.scale(small_text, (int(small_width * 4.5), int(small_height * 4.5)))
            
            # 居中绘制，并添加云朵浮动效果（跟随云朵一起移动）
            text_rect = pixel_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + cloud_float_offset))
            screen.blit(pixel_text, text_rect)
            
            # 如果达到5分，显示皇冠（像素风格）
            if score >= 5:
                # 绘制像素风格的皇冠
                crown_size = 60  # 皇冠大小
                crown_x = SCREEN_WIDTH // 2 - crown_size // 2
                crown_y = SCREEN_HEIGHT // 2 - 120 + cloud_float_offset  # 在文字上方更高位置，跟随云朵浮动
                
                # 绘制光束（从皇冠四周散发）
                beam_color = (255, 255, 150, 180)  # 淡黄色，半透明
                beam_length = 30
                beam_width = 4
                
                # 创建光束表面
                beam_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                
                # 8个方向的光束（上、下、左、右、四个对角）
                beam_angles = [0, 45, 90, 135, 180, 225, 270, 315]
                crown_center_x = crown_x + crown_size // 2
                crown_center_y = crown_y + crown_size // 2
                
                for angle in beam_angles:
                    # 计算光束终点
                    rad = math.radians(angle)
                    end_x = crown_center_x + math.cos(rad) * beam_length
                    end_y = crown_center_y + math.sin(rad) * beam_length
                    
                    # 绘制光束（从皇冠中心向外）
                    pygame.draw.line(beam_surface, beam_color, 
                                   (crown_center_x, crown_center_y), 
                                   (end_x, end_y), beam_width)
                    
                    # 在光束末端绘制像素风格的闪光点
                    spark_size = 6
                    pygame.draw.rect(beam_surface, (255, 255, 200, 200),
                                   (end_x - spark_size // 2, end_y - spark_size // 2, 
                                    spark_size, spark_size))
                
                # 绘制光束到屏幕
                screen.blit(beam_surface, (0, 0))
                
                # 创建皇冠表面
                crown_surface = pygame.Surface((crown_size, crown_size), pygame.SRCALPHA)
                
                # 皇冠颜色（金黄色）
                gold = (255, 215, 0)
                dark_gold = (218, 165, 32)
                
                pixel_size = crown_size // 12  # 像素块大小
                
                # 绘制皇冠的像素图案（12x12像素网格）
                crown_pattern = [
                    "            ",
                    "  XX    XX  ",
                    "  XX    XX  ",
                    " XXXX  XXXX ",
                    " XXXX  XXXX ",
                    "XXXXXXXXXXXX",
                    "XXXXXXXXXXXX",
                    "XXXXXXXXXXXX",
                    " XXXXXXXXXX ",
                    " XXXXXXXXXX ",
                    "  XXXXXXXX  ",
                    "            "
                ]
                
                # 绘制皇冠图案
                for row in range(12):
                    for col in range(12):
                        if crown_pattern[row][col] == 'X':
                            # 添加一些渐变效果
                            if col < 6:
                                color = gold
                            else:
                                color = dark_gold
                            pygame.draw.rect(crown_surface, color, 
                                           (col * pixel_size, row * pixel_size, pixel_size, pixel_size))
                
                # 添加宝石装饰（红色像素点）
                gem_positions = [(2, 6), (5, 6), (9, 6)]  # 三颗宝石位置
                gem_color = (255, 0, 0)
                for gem_col, gem_row in gem_positions:
                    pygame.draw.rect(crown_surface, gem_color,
                                   (gem_col * pixel_size, gem_row * pixel_size, pixel_size * 2, pixel_size * 2))
                
                # 绘制皇冠到屏幕
                screen.blit(crown_surface, (crown_x, crown_y))

        # 更新分数动画
        if score_animating:
            score_animation_frame += 1
            # 动画持续12帧（约0.4秒），更快速
            if score_animation_frame <= 6:
                # 前6帧：放大到1.5倍
                score_scale = 1.0 + (score_animation_frame / 6) * 0.5
            elif score_animation_frame <= 12:
                # 后6帧：缩小回1.0倍
                score_scale = 1.5 - ((score_animation_frame - 6) / 6) * 0.5
            else:
                # 动画结束
                score_scale = 1.0
                score_animating = False
                score_animation_frame = 0
        
        # 如果达到5分，持续循环闪烁动画
        if score >= 5:
            score_animation_frame += 1
            # 循环动画：每12帧一个周期
            cycle_frame = score_animation_frame % 12
            if cycle_frame <= 6:
                # 前6帧：放大到1.3倍
                score_scale = 1.0 + (cycle_frame / 6) * 0.3
            else:
                # 后6帧：缩小回1.0倍
                score_scale = 1.3 - ((cycle_frame - 6) / 6) * 0.3

        # 在右下角显示分数文字（带缩放动画和颜色变化）
        score_font = pygame.font.Font(None, 36)
        score_color = get_score_color(score)  # 根据分数获取颜色
        score_text = score_font.render(f"Score: {score}", True, score_color)
        
        # 如果有缩放动画，缩放文字
        if score_scale != 1.0:
            scaled_width = int(score_text.get_width() * score_scale)
            scaled_height = int(score_text.get_height() * score_scale)
            score_text = pygame.transform.scale(score_text, (scaled_width, scaled_height))
        
        score_rect = score_text.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10))
        screen.blit(score_text, score_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

    # 修改主循环，添加气球动画
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # 清屏（白色背景）
        screen.fill((255, 255, 255))

        # 更新并绘制所有气球
        for balloon in balloons:
            balloon.update()
            balloon.draw(screen)

        # 显示提示文字
        text = font.render("按ESC退出", True, (100, 100, 100))
        screen.blit(text, (10, 10))

        # 刷新屏幕
        pygame.display.flip()
        clock.tick(60)