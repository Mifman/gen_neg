# Библиотеки
import random as rdm
from time import sleep as slp
from os import system
import copy

# Файлы для работы проекта
from draw import *
from b_action import *
from gen_bots import *
from gen_const import *
from gen_room import *
from genesis import *

score = 0
score_last = 0
gen_step = 1
score_best = 0
room = create_room(ROOM_SIZE)
bots = generate_bots()
room = relocate_bots(room, bots)

while True:
    food_tick_count = 0

    while len(bots) > POPULATION_LEFT:
        food_tick_count += 1

        if food_tick_count == CREATE_FOOD_TICK: # Генерация еды
            food_type, food_coord = create_food(ROOM_SIZE)
            while room[food_coord[0]][food_coord[1]] != ' ':
                food_type, food_coord = create_food(ROOM_SIZE)
            room[food_coord[0]][food_coord[1]] = food_type
            food_tick_count = 0

        for b in range(len(bots)):
            room, bots[b].coords, bots[b].hp, bots[b].brain, bots[b].step, bots[b].direction, bots[b].make_time = bot_action(room, bots[b].coords, bots[b].hp, bots[b].brain,
                                                                                         bots[b].step, bots[b].direction, bots[b].make_time, b)

        del_bots = [] # Инициализируем список с мёртвыми ботами
        for d in range(len(bots)):
            if bots[d].hp <= 0:
                del_bots.append(bots[d])

        # На случай, если все боты умерли
        dead_count = len(del_bots)
        if dead_count == len(bots):
            dead_count -= 8

        for d in range(dead_count):
            bots.remove(del_bots[d])

        room = relocate_bots(room, bots)
        display_array(room, score, gen_step, bots, score_best, score_last)
        #slp(0.1)
        score += 1

    gen_step += 1 # Обновляем номер поколения
    if score > score_best: # Обнуляем счётчик тиков лучшего поколения
        score_best = copy.deepcopy(score)
    score_last = copy.deepcopy(score)
    score = 0

    n_bots = [] # Инициализируем список с новыми ботами
    bots = change_amount(bots)
    for n in range(POPULATION_LEFT):
        for nn in range(POPULATION_LEFT): # Возведение с степень POPULATION_LEFT
            n_bots += generation([0,0], bots[n].hp, bots[n].brain, bots[n].step, bots[n].direction, bots[n].make_time, nn)

    bots = generate_bots() # Полное говнище, но мне лень фиксить. Каждый раз генериться новый список с ботами
    for nn in range(POPULATION):
        bots[nn].coords, bots[nn].hp, bots[nn].brain, bots[nn].step,\
            bots[nn].direction, bots[nn].make_time = create_coord_bot(room, ROOM_SIZE), n_bots[nn][1], n_bots[nn][2], n_bots[nn][3], \
                                                    n_bots[nn][4], n_bots[nn][5]
    room = create_room(ROOM_SIZE)
    room = relocate_bots(room, bots)
