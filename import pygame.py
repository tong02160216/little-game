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
BACKGROUND = (200, 200, 200)  # 淡灰色背景
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

def draw_maze(maze, start):
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
    
    # 绘制起点的灰色圆形和文字“START”
    sx, sy = start
    pygame.draw.circle(screen, (128, 128, 128), (sx * CELL_SIZE + CELL_SIZE // 2, sy * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3 * 2)  # 灰色圆形
    font = pygame.font.SysFont(None, 18)  # 使用默认字体，字号为18，确保文字不超过圆的直径
    text_surface = font.render("START", True, (255, 255, 255))  # 白色文字
    text_rect = text_surface.get_rect(center=(sx * CELL_SIZE + CELL_SIZE // 2, sy * CELL_SIZE + CELL_SIZE // 2))
    screen.blit(text_surface, text_rect)
    
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

# 加载多个气球背景图像
balloon_images = [
    pygame.image.load("F:/code/little_game/B1.png"),
    pygame.image.load("F:/code/little_game/B2.png"),
    pygame.image.load("F:/code/little_game/B3.png"),
    pygame.image.load("F:/code/little_game/B4.png"),
    pygame.image.load("F:/code/little_game/B5.png"),
    pygame.image.load("F:/code/little_game/B6.png"),
    pygame.image.load("F:/code/little_game/B7.png")
]

# 定义气球类
class Balloon:
    def __init__(self):
        # 随机大小（控制远近，小的看起来远）
        self.scale = random.uniform(0.5, 1.5)  # 随机缩放比例
        self.image = random.choice(balloon_images)  # 随机选择气球图像
        self.image = pygame.transform.scale(
            self.image, (
                int(self.image.get_width() * self.scale),
                int(self.image.get_height() * self.scale)
            )
        )

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
    HOUSE_IMAGE = pygame.image.load("F:/code/little_game/房子2.png")
    HOUSE_IMAGE = pygame.transform.scale(HOUSE_IMAGE, (CELL_SIZE * 2, CELL_SIZE * 2))  # 调整房子大小

    # 生成迷宫
    maze, start, end = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)  # 获取终点位置
    player_x, player_y = start
    end_x, end_y = end

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

        draw_maze(maze, start)

        # 调整蜗牛的位置，使其居中于迷宫单元格
        snail_offset_x = (CELL_SIZE * 3 - CELL_SIZE) // 2
        snail_offset_y = (CELL_SIZE * 3 - CELL_SIZE) // 2
        screen.blit(PLAYER_IMAGE, (player_x * CELL_SIZE - snail_offset_x, player_y * CELL_SIZE - snail_offset_y))

        # 调整房子的位置稍微向下
        house_offset_x, house_offset_y = -CELL_SIZE // 2, -CELL_SIZE + CELL_SIZE // 4
        screen.blit(HOUSE_IMAGE, ((end_x * CELL_SIZE) + house_offset_x, (end_y * CELL_SIZE) + house_offset_y))

        # 检查蜗牛是否到达房子
        if player_x == end_x and player_y == end_y:
            font = pygame.font.Font(None, 74)
            text = font.render("Congratulations!!", True, (0, 255, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

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