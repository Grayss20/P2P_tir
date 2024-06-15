import pygame
from random import randint

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Задаем иконку
pygame.display.set_caption('Игра в тир')
icon = pygame.image.load('images/shooter.jpg')
pygame.display.set_icon(icon)
# Задаем цель
target_image = pygame.image.load('images/gangster.png')
target_width = 80
target_height = 100
# Задаем фоновый рисунок
color = (randint(0, 255), randint(0, 255), randint(0, 255))

target_x = randint(0, SCREEN_WIDTH - target_width)
target_y = randint(0, SCREEN_HEIGHT - target_height)


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (target_x<mouse_x<target_x+target_width) and \
                    (target_y <mouse_y <target_y+target_height):
                target_x = randint(0, SCREEN_WIDTH - target_width)
                target_y = randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

pygame.quit()
