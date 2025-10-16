import pygame
import sys

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y - radius > 0:
        y -= speed
    if keys[pygame.K_s] and y + radius < HEIGHT:
        y += speed
    if keys[pygame.K_a] and x - radius > 0:
        x -= speed
    if keys[pygame.K_d] and x + radius < WIDTH:
        x += speed

    screen.fill((0, 0, 0))  # 黑色背景
    pygame.draw.circle(screen, (255, 255, 255), (x, y), radius)  # 白色圆点
    pygame.display.flip()
    clock.tick(60)