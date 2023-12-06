from gen_const import *
import random as rdm
from time import sleep as slp

id_objects = ['&', '#', '@', '*', ' '] # ID объектов

def step_overflow(step):
    if step > 63:
        step -= 63
    return step

def bot_action(room, coords, hp, brain, step, direction, make_time, bots_amount):
    global id_objects
    step = step_overflow(step)

    if hp <= 0:
        return room, coords, hp, brain, step, direction, make_time


    if make_time == MAKE_TIME_MAX:
        hp -= 1
        return room, coords, hp, brain, step, direction, make_time

    if brain[step] <= 7:
        room, coords, hp, brain, step, direction, make_time = bot_move(room, coords, hp, brain, step, direction, make_time)
        step = step_overflow(step)
        hp -= 1

    elif brain[step] > 7 and brain[step] <= 15:
        room, coords, hp, brain, step, direction, make_time = bot_eat(room, coords, hp, brain, step, direction, make_time)
        step = step_overflow(step)
        hp -= 1

    elif brain[step] > 15 and brain[step] <= 23:
        step += bot_look(room, coords, direction)

        step = step_overflow(step)
        make_time += 1
        return bot_action(room, coords, hp, brain, step, direction, make_time, bots_amount)

    elif brain[step] > 23 and brain[step] <= 31:
        direction = brain[step]

        step += 1
        step = step_overflow(step)
        make_time += 1
        return bot_action(room, coords, hp, brain, step, direction, make_time, bots_amount)

    elif brain[step] > 31:
        step += brain[step]

        step = step_overflow(step)

        make_time += 1
        return bot_action(room, coords, hp, brain, step, direction, make_time, bots_amount)

    return room, coords, hp, brain, step, direction, make_time


def bot_move(room, coords, hp, brain, step, direction, make_time):
    global id_objects

    # Вверх
    if direction == 24:
        if room[coords[0] - 1][coords[1]] == '*':
            hp += EAT_INCREMENT
            step += id_objects.index('*')
            coords = [coords[0] - 1, coords[1]]
        elif room[coords[0] - 1][coords[1]] == ' ':
            coords = [coords[0] - 1, coords[1]]
            step += id_objects.index(' ')

        elif room[coords[0] - 1][coords[1]] == '&':
            hp -= POISON_DAMAGE
            step += id_objects.index('&')
            coords = [coords[0] - 1, coords[1]]

    # Вверх-вправо
    elif direction == 25:
        if room[coords[0] - 1][coords[1] + 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            coords = [coords[0] - 1, coords[1] + 1]

        elif room[coords[0] - 1][coords[1] + 1] == ' ':
            step += id_objects.index(' ')
            coords = [coords[0] - 1, coords[1] + 1]

        elif room[coords[0] - 1][coords[1] + 1] == '&':
            step += id_objects.index('&')
            hp -= POISON_DAMAGE
            coords = [coords[0] - 1, coords[1] + 1]

    # Вправо
    elif direction == 26:
        if room[coords[0]][coords[1] + 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            coords = [coords[0], coords[1] + 1]

        elif room[coords[0]][coords[1] + 1] == ' ':
            step += id_objects.index(' ')
            coords = [coords[0], coords[1] + 1]

        elif room[coords[0]][coords[1] + 1] == '&':
            step += id_objects.index('&')
            hp -= POISON_DAMAGE
            coords = [coords[0], coords[1] + 1]

    # Вниз-Вправо
    elif direction == 27:
        if room[coords[0] + 1][coords[1] + 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            coords = [coords[0] + 1, coords[1] + 1]

        elif room[coords[0] + 1][coords[1] + 1] == ' ':
            step += id_objects.index(' ')
            coords = [coords[0] + 1, coords[1] + 1]

        elif room[coords[0] + 1][coords[1] + 1] == '&':
            step += id_objects.index('&')
            hp -= POISON_DAMAGE
            coords = [coords[0] + 1, coords[1] + 1]

    # Вниз
    elif direction == 28:
        if room[coords[0] + 1][coords[1]] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            coords = [coords[0] + 1, coords[1]]

        elif room[coords[0] + 1][coords[1]] == ' ':
            step += id_objects.index(' ')
            coords = [coords[0] + 1, coords[1]]

        elif room[coords[0] + 1][coords[1]] == '&':
            step += id_objects.index('&')
            hp -= POISON_DAMAGE
            coords = [coords[0] + 1, coords[1]]

    # Вниз-влево
    elif direction == 29:
        if room[coords[0] + 1][coords[1] - 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            coords = [coords[0] + 1, coords[1] - 1]

        elif room[coords[0] + 1][coords[1] - 1] == ' ':
            step += id_objects.index(' ')
            coords = [coords[0] + 1, coords[1] - 1]

        elif room[coords[0] + 1][coords[1] - 1] == '&':
            step += id_objects.index('&')
            hp -= POISON_DAMAGE
            coords = [coords[0] + 1, coords[1] - 1]

    # Влево
    elif direction == 30:
        if room[coords[0]][coords[1] - 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            coords = [coords[0], coords[1] - 1]

        elif room[coords[0]][coords[1] - 1] == ' ':
            step += id_objects.index(' ')
            coords = [coords[0], coords[1] - 1]

        elif room[coords[0]][coords[1] - 1] == '&':
            step += id_objects.index('&')
            hp -= POISON_DAMAGE
            coords = [coords[0], coords[1] - 1]

    # Влево-вверх
    elif direction == 31:
        if room[coords[0] - 1][coords[1] - 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            coords = [coords[0] - 1, coords[1] - 1]

        elif room[coords[0] - 1][coords[1] - 1] == ' ':
            step += id_objects.index(' ')
            coords = [coords[0] - 1, coords[1] - 1]

        elif room[coords[0] - 1][coords[1] - 1] == '&':
            step += id_objects.index('&')
            hp -= POISON_DAMAGE
            coords = [coords[0] - 1, coords[1] - 1]

    return room, coords, hp, brain, step, direction, make_time

def bot_eat(room, coords, hp, brain, step, direction, make_time):
    global id_objects

    # Вверх
    if direction == 24:
        if room[coords[0] - 1][coords[1]] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            room[coords[0] - 1][coords[1]] = ' '

        elif room[coords[0] - 1][coords[1]] == '&':
            room[coords[0] - 1][coords[1]] = '*'
            step += id_objects.index('*')

    # Вверх-вправо
    elif direction == 25:
        if room[coords[0] - 1][coords[1] + 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            room[coords[0] - 1][coords[1] + 1] = ' '

        elif room[coords[0] - 1][coords[1] + 1] == '&':
            room[coords[0] - 1][coords[1] + 1] = '*'
            step += id_objects.index('*')

    # Вправо
    elif direction == 26:
        if room[coords[0]][coords[1] + 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            room[coords[0]][coords[1] + 1] = ' '

        elif room[coords[0]][coords[1] + 1] == '&':
            step += id_objects.index('*')
            room[coords[0]][coords[1] + 1] = '*'

    # Вниз-Вправо
    elif direction == 27:
        if room[coords[0] + 1][coords[1] + 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            room[coords[0] + 1][coords[1] + 1] = ' '

        elif room[coords[0] + 1][coords[1] + 1] == '&':
            step += id_objects.index('*')
            room[coords[0] + 1][coords[1] + 1] = '*'

    # Вниз
    elif direction == 28:
        if room[coords[0] + 1][coords[1]] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            room[coords[0] + 1][coords[1]] = ' '

        elif room[coords[0] + 1][coords[1]] == '&':
            step += id_objects.index('*')
            room[coords[0] + 1][coords[1]] = '*'

    # Вниз-влево
    elif direction == 29:
        if room[coords[0] + 1][coords[1] - 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            room[coords[0] + 1][coords[1] - 1] = ' '

        elif room[coords[0] + 1][coords[1] - 1] == '&':
            step += id_objects.index('*')
            room[coords[0] + 1][coords[1] - 1] = '*'

    # Влево
    elif direction == 30:
        if room[coords[0]][coords[1] - 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            room[coords[0]][coords[1] - 1] = ' '

        elif room[coords[0]][coords[1] - 1] == '&':
            step += id_objects.index('*')
            room[coords[0]][coords[1] - 1] = '*'

    # Влево-вверх
    elif direction == 31:
        if room[coords[0] - 1][coords[1] - 1] == '*':
            step += id_objects.index('*')
            hp += EAT_INCREMENT
            room[coords[0] - 1][coords[1] - 1] = ' '

        elif room[coords[0] - 1][coords[1] - 1] == '&':
            step += id_objects.index('*')
            room[coords[0] - 1][coords[1] - 1] = '*'

    return room, coords, hp, brain, step, direction, make_time

def bot_look(room, coords, direction):
    global id_objects

    # Вверх
    if direction == 24:
        return id_objects.index(room[coords[0] - 1][coords[1]])

    # Вверх-вправо
    elif direction == 25:
        return id_objects.index(room[coords[0] - 1][coords[1] + 1])

    # Вправо
    elif direction == 26:
        return id_objects.index(room[coords[0]][coords[1] + 1])

    # Вниз-Вправо
    elif direction == 27:
        return id_objects.index(room[coords[0] + 1][coords[1] + 1])

    # Вниз
    elif direction == 28:
        return id_objects.index(room[coords[0] + 1][coords[1]])

    # Вниз-влево
    elif direction == 29:
        return id_objects.index(room[coords[0] + 1][coords[1] - 1])

    # Влево
    elif direction == 30:
        return id_objects.index(room[coords[0]][coords[1] - 1])

    # Влево-вверх
    elif direction == 31:
        return id_objects.index(room[coords[0] - 1][coords[1] - 1])
