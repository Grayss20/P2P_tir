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
color = (randint(0,255), randint)

target_x = randint(0, SCREEN_WIDTH - target_width)
target_y = randint(0, SCREEN_HEIGHT - target_height)
color = (randint(0, 255), randint(0, 255), randint(0, 255))

running = True
while running:
    pass

pygame.quit()
