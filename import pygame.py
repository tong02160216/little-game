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
# 修改Pygame窗口标题
pygame.display.set_caption("送蜗牛回家")

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
BACKGROUND = (200, 200, 200)  # 淡灰色背景
WALL = (255, 255, 255)        # 白色墙线
ARROW = (0, 0, 0)             # 起点黑色箭头

# 加载终点红旗图片
FLAG_IMAGE = pygame.image.load("F:/code/little_game/red flag.png")
FLAG_IMAGE = pygame.transform.scale(FLAG_IMAGE, (CELL_SIZE * 2, CELL_SIZE * 2))  # 调整红旗大小
# 加载玩家图片
PLAYER_IMAGE = pygame.image.load("F:/code/little_game/022-snails.png")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))  # 调整玩家图片大小

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("随机迷宫生成器")

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
    
    # 设置终点在右下角
    end_x, end_y = width - 2, height - 2
    maze[end_y][end_x] = 0
    
    return maze, (start_x, start_y), (end_x, end_y)

def draw_maze(maze, start, end):
    """绘制迷宫"""
    screen.fill(BACKGROUND)
    
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                # 绘制墙
                rect = pygame.Rect(
                    x * CELL_SIZE, 
                    y * CELL_SIZE, 
                    CELL_SIZE, 
                    CELL_SIZE
                )
                pygame.draw.rect(screen, WALL, rect)
    
    # 绘制起点的圆形和文字“START”
    sx, sy = start
    pygame.draw.circle(screen, (0, 0, 0), (sx * CELL_SIZE + CELL_SIZE // 2, sy * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3 * 2)  # 黑色圆形
    font = pygame.font.SysFont(None, 18)  # 使用默认字体，字号为18，确保文字不超过圆的直径
    text_surface = font.render("START", True, (255, 255, 255))  # 白色文字
    text_rect = text_surface.get_rect(center=(sx * CELL_SIZE + CELL_SIZE // 2, sy * CELL_SIZE + CELL_SIZE // 2))
    screen.blit(text_surface, text_rect)
    
    # 绘制终点的红色圆形和文字“END”
    ex, ey = end
    pygame.draw.circle(screen, (255, 0, 0), (ex * CELL_SIZE + CELL_SIZE // 2, ey * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3 * 2)  # 红色圆形
    end_text_surface = font.render("END", True, (255, 255, 255))  # 白色文字
    end_text_rect = end_text_surface.get_rect(center=(ex * CELL_SIZE + CELL_SIZE // 2, ey * CELL_SIZE + CELL_SIZE // 2))
    screen.blit(end_text_surface, end_text_rect)
    
    pygame.display.flip()

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

# 创建静态背景
static_background = generate_static_pixel_background(WIDTH, HEIGHT, 20)

# 添加蜗牛到达终点的动画函数
def play_celebration_animation():
    # 设置画布
    screen = turtle.Screen()
    screen.setup(600, 400)
    screen.title("庆祝")
    screen.bgcolor("black")

    # 创建爱心
    heart = turtle.Turtle()
    heart.color("red")
    heart.shape("circle")  # 先用圆形，后续画爱心
    heart.penup()
    heart.speed(0)

    # 爱心的绘制函数
    def draw_heart(size):
        heart.pendown()
        heart.begin_fill()
        heart.left(140)
        heart.forward(size)
        heart.circle(-size/2, 180)
        heart.left(120)
        heart.circle(-size/2, 180)
        heart.forward(size)
        heart.end_fill()
        heart.penup()
        heart.setheading(0)  # 重置方向

    # 弹跳参数
    x, y = 0, 0
    dx, dy = 3, 4  # 速度
    size = 30

    # 动画循环
    for _ in range(100):  # 循环100次
        screen.clear()
        heart.goto(x, y)
        draw_heart(size)
        # 更新位置（碰到边界反弹）
        x += dx
        y += dy
        if x > 300 - size or x < -300 + size:
            dx *= -1
        if y > 200 - size or y < -200 + size:
            dy *= -1
        time.sleep(0.05)

    turtle.write("🎉 庆祝！🎉", align="center", font=("Arial", 20, "bold"))
    turtle.hideturtle()
    turtle.done()

# 添加结算画面的函数，使用气球图像
def show_congratulations_screen():
    # 加载背景图像作为气球背景
    background_image = pygame.image.load("F:/code/little_game/生成气球图片.png")

    # 加载背景气球图像
    background_balloon_image = pygame.image.load("F:/code/little_game/生成气球图片.png")

    # 初始化背景气球参数
    background_balloons = []
    for _ in range(20):  # 创建20个背景气球
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 300)
        dy = random.uniform(-3, -1)  # 较慢的上升速度
        scale = random.uniform(0.5, 1.5)  # 大小范围
        background_balloons.append({'x': x, 'y': y, 'dy': dy, 'scale': scale})

    # 在结算画面中绘制背景气球动画
    while True:  # 无限循环，保持画面
        screen.fill((255, 255, 255))  # 白色背景

        # 绘制背景气球
        for balloon in background_balloons:
            scaled_balloon = pygame.transform.scale(background_balloon_image, (
                int(background_balloon_image.get_width() * balloon['scale']),
                int(background_balloon_image.get_height() * balloon['scale'])
            ))
            screen.blit(scaled_balloon, (balloon['x'], balloon['y']))
            balloon['y'] += balloon['dy']
            if balloon['y'] + scaled_balloon.get_height() < 0:
                balloon['y'] = SCREEN_HEIGHT + random.randint(0, 200)
                balloon['x'] = random.randint(0, SCREEN_WIDTH)
                balloon['scale'] = random.uniform(0.5, 1.5)

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

# 定义气球类
class Balloon:
    def __init__(self):
        # 随机大小（控制远近，小的看起来远）
        self.size = random.randint(15, 40)
        # 随机位置（从底部开始）
        self.x = random.randint(self.size, SCREEN_WIDTH - self.size)
        self.y = SCREEN_HEIGHT + self.size

        # 随机颜色
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

        # 速度设置（小气球速度慢，模拟远处效果）
        self.speed = (self.size / 40) * 2 + random.uniform(0.5, 1.5)

        # 左右摇摆幅度和速度
        self.swing_amplitude = random.uniform(0.5, 2.0)
        self.swing_speed = random.uniform(0.02, 0.05)
        self.swing_offset = random.uniform(0, math.pi * 2)

        # 绳子长度
        self.string_length = self.size * 1.2

    def update(self):
        # 向上移动
        self.y -= self.speed

        # 左右摇摆（使用正弦函数实现平滑摇摆）
        self.x += math.sin(pygame.time.get_ticks() * 0.001 * self.swing_speed + self.swing_offset) * self.swing_amplitude

        # 当气球飞出屏幕顶部时重置位置
        if self.y < -self.size * 2:
            self.reset()

    def reset(self):
        # 重置气球到屏幕底部
        self.x = random.randint(self.size, SCREEN_WIDTH - self.size)
        self.y = SCREEN_HEIGHT + self.size
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

    def draw(self, surface):
        # 绘制气球主体
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)

        # 绘制气球高光（增加立体感）
        highlight_color = (
            min(255, self.color[0] + 50),
            min(255, self.color[1] + 50),
            min(255, self.color[2] + 50)
        )
        pygame.draw.circle(
            surface, 
            highlight_color, 
            (int(self.x - self.size/3), int(self.y - self.size/3)), 
            self.size // 5
        )

        # 绘制气球底部
        pygame.draw.polygon(
            surface, 
            self.color, 
            [
                (self.x - self.size//5, self.y + self.size//5),
                (self.x, self.y + self.size//2),
                (self.x + self.size//5, self.y + self.size//5)
            ]
        )

        # 绘制绳子
        pygame.draw.line(
            surface, 
            (50, 50, 50), 
            (self.x, self.y + self.size//2),
            (self.x, self.y + self.size//2 + self.string_length),
            1 if self.size < 25 else 2  # 小气球绳子细一些
        )

# 创建气球列表
balloons = [Balloon() for _ in range(40)]  # 40个气球

# 确保字体初始化在主循环之前完成
pygame.font.init()
font = pygame.font.SysFont(["SimHei", "WenQuanYi Micro Hei", "Heiti TC"], 30)

# 定义 main 函数

def main():
    # 初始化 Pygame
    pygame.init()

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
    PLAYER_IMAGE = pygame.image.load("F:/code/little_game/022-snails.png")
    PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (CELL_SIZE, CELL_SIZE))

    # 生成迷宫
    maze, start, end = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
    player_x, player_y = start

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

        draw_maze(maze, start, end)
        screen.blit(PLAYER_IMAGE, (player_x * CELL_SIZE, player_y * CELL_SIZE))
        pygame.display.flip()
        clock.tick(30)

        if (player_x, player_y) == end:
            show_congratulations_screen()
            running = False

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