import pygame
from random import choice
import time

pygame.init()
# Размеры окна
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 683
# Размеры цели
TARGET_WIDTH = 40
TARGET_HEIGHT = 75
# Координаты окон в здании
windows_x = [205, 437, 550, 764]
windows_y = 425
# Время реакции  в секундах
DELAY = 2
# Типы целей
targets = ('girl', 'bandit')
# Счетчик убитых
kill_girl = 0
kill_bandit = 0
kill_user = 0


def target_type(x, y):
    ''' Выбирает и отрисовывает случайную мишень, возвращет тип мишени'''
    if choice(targets) == 'girl':
        screen.blit(girl_image, (x, y))
        return 'girl'  # Мишень - девушка
    screen.blit(bandit_image, (x, y))
    return 'bandit'  # Мищень - бандит


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Задаем шрифты
pygame.font.init()
font_path = pygame.font.match_font('arial')
my_font = pygame.font.Font(font_path, 30)
# Задаем иконку
pygame.display.set_caption('Дикий, очень дикий Запад')
icon = pygame.image.load('Images/shooter.jpg')
pygame.display.set_icon(icon)
# Задаем бандита
bandit_image = pygame.image.load('images/bandit.png')
# Задаем мирного жителя
girl_image = pygame.image.load('images/girl.png')
# Задаем фоновый рисунок
bg = pygame.image.load('images/bg.jpg')
# Меняем форму курсора мыши
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
running = True
while running:
    screen.blit(bg, (0, 0))
    target_x = choice(windows_x)
    target_y = windows_y
    target = target_type(target_x, target_y)
    start_time = time.time()
    # Переменная, которая фиксирует попадание в цель
    hit = False
    message = my_font.render(f'Убито гражданских {kill_girl}  Убито бандитов {kill_bandit} '
                             f'Убито пользователей {kill_user}', True, (0, 0, 0), )
    screen.blit(message, (0, 0))
    pygame.display.update()
    # Пользователь должен успеть выстрелить за DELAY секунд
    while time.time() - start_time < DELAY:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (target_x < mouse_x < target_x + TARGET_WIDTH) and \
                        (target_y < mouse_y < target_y + TARGET_HEIGHT):
                    if target == 'bandit':
                        kill_bandit += 1
                        hit = True
                        break
                    if target == 'girl':
                        kill_girl += 1
                        hit = True
                        break
    if target == 'bandit' and not hit:
        kill_user += 1
pygame.quit()
