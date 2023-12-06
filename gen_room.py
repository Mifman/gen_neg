import random as rdm
from gen_const import *
from draw import *
import time

# ГЕНЕРАЦИЯ КОМНАТЫ
##############
def rand_room(x):
    l = []
    for a in range(x):
        if a == 0 or a == (x - 1):
            l.append('#')
        else:
            l.append(rdm.choice(LIST_EL))
    return l

def wall_room(x):
    l = []
    for a in range(x):
        l.append('#')
    return l

def wall_middle1(x):
    return list('#' + (' ' * 4) + ('#' * 5) + (' ' * 20) + ('#' * 5) + (' ' * 9 + '#')) # Создаём стеночки (сделано для комнаты 45x45!)

def wall_middle2(x):
    return list('#' + (' ' * 9) + ('#' * 8) + (' ' * 17) + ('#' * 10)) # Создаём стеночки (сделано для комнаты 45x45!)

def wall_up(x):
    global LIST_EL
    l = []
    for a in range(x):
        if a == 0 or a == (x - 1) or a == int(x/2):
            l.append('#')

        else:
            l.append(rdm.choice(LIST_EL))
    return l

def create_food(size_room): # Генерация еды во время игры (возвращает тип еды и координаты спавна)
    return rdm.choice(['*', '&']), [rdm.randint(1, size_room - 2), rdm.randint(1, size_room - 2)]
##############

def create_room(generate_room):
    r = []
    for i in range(generate_room):  # Генерируем комнату
        if i == 0 or i == (generate_room - 1):
            r.append(wall_room(generate_room))

        elif i == int(generate_room / 2):
            r.append(wall_middle1(generate_room))

        elif i == generate_room - 10:
            r.append(wall_middle2(generate_room))

        elif (i < 15 and i > 0 and i != (generate_room - 1)) or (i >= generate_room - 15 and i != (generate_room - 1)): # для 45x45
            r.append(wall_up(generate_room))

        else:
            r.append(rand_room(generate_room))

    #r = relocate_bots(r, bots)
    return r

# ПЕРЕМЕЩЕНИЕ БОТОВ
##############
def relocate_bots(room, bots): # Перемещение ботов по полю (перенос на основе координат)
    bot_coord = []

    for bot in bots:
        bot_coord.append(bot.coords)

    for i in range(len(room)):
        for ii in range(len(room[i])):
            delete = True
            for bot in bot_coord:
                if i == bot[0] and ii == bot[1]:
                    room[i][ii] = '@'
                    delete = False

            if delete and room[i][ii] == '@':
                room[i][ii] = ' '

    return room

room = create_room(ROOM_SIZE)