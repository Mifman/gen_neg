import pygame
from time import sleep as slp

# Размеры окна PyGame
width, height = 800, 800

# Инициализация PyGame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Generation v0.7")

# Определение цветов
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)


def display_array(array, score, gen_step, bots, score_best, score_last):
    global width
    global height
    # Размеры поля с символами
    array_width = len(array[0])
    array_height = len(array)

    # Размер каждой ячейки
    cell_width = width // array_width
    cell_height = height // array_height

    # Отображение поля с символами
    for row in range(array_height):
        for col in range(array_width):
            cell = array[row][col]
            x = col * cell_width
            y = row * cell_height

            if cell == ' ':
                color = BLACK
            if cell == '*':
                color = GREEN
            elif cell == '&':
                color = RED
            elif cell == '@':
                color = BLUE
            elif cell == '#':
                color = GRAY

            pygame.draw.rect(screen, color, (x, y, cell_width, cell_height))
    print('\nТик:', score, end=' | ')
    print('Лучший счёт:', score_best)
    print('Предыдущий счёт:', score_last)
    print('Поколение:', gen_step, end=' | ')
    print('Кол-во ботов:', len(bots))
    #pygame.display.flip()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()