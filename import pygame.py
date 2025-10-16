import pygame
import sys
import random

# 初始化
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("白色小圆点移动")

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

def main():
    clock = pygame.time.Clock()
    # 生成迷宫
    maze, start, end = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
    
    # 玩家初始位置
    player_x, player_y = start

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 按空格键重新生成迷宫
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    maze, start, end = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
                    player_x, player_y = start

        # 获取按键状态
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and maze[player_y - 1][player_x] == 0:  # 向上移动
            player_y -= 1
        if keys[pygame.K_s] and maze[player_y + 1][player_x] == 0:  # 向下移动
            player_y += 1
        if keys[pygame.K_a] and maze[player_y][player_x - 1] == 0:  # 向左移动
            player_x -= 1
        if keys[pygame.K_d] and maze[player_y][player_x + 1] == 0:  # 向右移动
            player_x += 1

        draw_static_pixel_background(screen, static_background)  # 使用静态像素块背景
        pygame.draw.circle(screen, (255, 255, 255), (x, y), radius)  # 白色圆点
        draw_maze(maze, start, end)
        # 绘制玩家
        screen.blit(PLAYER_IMAGE, (player_x * CELL_SIZE, player_y * CELL_SIZE))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()