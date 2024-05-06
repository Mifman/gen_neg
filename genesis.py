"""
Симуляция генетического алгоритма
Версия: 0.4
"""

# Библиотеки
import random as rdm
from time import sleep as slp
import copy

# Файлы для работы проекта
from draw import *
from b_action import *
from gen_bots import *
from gen_const import *
from gen_room import *

def crossing_bots(bot1, bot2):
    point = rdm.randint(25,45)
    return bot1[point:] + bot2[:point]

def generate_bots(save=''):
    bots = []  # Список с ботами

    for i in range(POPULATION):
        bots.append(copy.deepcopy(create_bot()))

    if save != '': # Если грузим поколения с сохранения...
        for i in range(POPULATION):
            bots[i].brain = save[i]

    return bots

def change_amount(bots):
    while len(bots) < POPULATION_LEFT:
        bots.append(copy.deepcopy(bots[rdm.randint(0,len(bots) - 1)]))
    return bots

def generation(coords, hp, brain, step, direction, make_time, bot_count):
    new_bots = [[coords, BOT_HP, brain, 0, direction, 0]] # Список с новыми ботами

    for i in range(POPULATION_LEFT - 1):
        new_bots.append(copy.deepcopy(new_bots[0]))

    for i in range(len(new_bots)):
        new_bots[i][0] = create_coord_bot(room, ROOM_SIZE)
        new_bots[i][4] = rdm.randint(24, 31)

    # Мутация гена
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
