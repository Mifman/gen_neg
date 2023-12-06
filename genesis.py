"""
Симуляция генетического алгоритма
Версия: 0.4
"""

# Библиотеки
import random as rdm

# Файлы для работы проекта
from draw import *
from b_action import *
from gen_bots import *
from gen_const import *
from gen_room import *

def crossing_bots(bot1, bot2):
    point = rdm.randint(25,45)
    return bot1[point:] + bot2[:point]

def generate_bots():
    bots = []  # Список с ботами

    for i in range(POPULATION):
        bots.append(create_bot())

    return bots

def change_amount(bots):
    while len(bots) < POPULATION_LEFT:
        bots.append(bots[rdm.randint(0,len(bots) - 1)])
    return bots

def generation(coords, hp, brain, step, direction, make_time, bot_count):
    new_bots = [[coords, hp, brain, step, direction, make_time]] # Список с новыми ботами
    for i in range(POPULATION_LEFT - 2): # -2 Погрешность с отсчётом с 0 и факт, что 1 бот уже есть
        new_bots[i][0] = create_coord_bot(room, ROOM_SIZE)
        new_bots[i][1] = BOT_HP
        new_bots[i][3] = 0
        new_bots[i][4] = rdm.randint(24, 31)
        new_bots[i][5] = 0
        new_bots.append(new_bots[0])

    # Мутация гена
    mutation_begin = int(POPULATION / MAX_MUTATION) # Расчёт, через какое время производить мутанта
    if bot_count % mutation_begin == 0:
        for mut in range(rdm.randint(1,MAX_MUTATION_BOT)):
            new_bots[len(new_bots) - 1][2][rdm.randint(0,63)] = rdm.randint(0,63)

    # Скрещивание
    """
    count = 2
    for cross in range(len(new_bots)):
        if count % 3 == 0:
            new_bots[cross][2] = crossing_bots(new_bots[cross][2], new_bots[cross - 1][2])

        count += 1
    """
    return new_bots
