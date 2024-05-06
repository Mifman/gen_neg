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

### ЗАГРУЗКА СОХРАНЕНИЯ
is_load_save = False
save = input('Введите полное названия файла сохранения (оставьте пустым, чтобы не загружать)\n\n===>')
if save != '':
    is_load_save = True
    save = str(open(save).read()).split('\n')
    save = [(s.replace('[', '').replace(']', '').replace(' ', '')).split(',') for s in save] # Преобразование в список
    save.pop(64)
    save = [[int(i) for i in s] for s in save] # Преобразование каждого числа в тип int
    print(save[0])

###

score = 0
score_last = 0
gen_step = 1
score_best = 0
room = create_room(ROOM_SIZE)
room = create_food_in_room(room, ROOM_SIZE)
bots = generate_bots(save)
room = relocate_bots(room, bots)
food = food_count(room)

count_for_save = 0 # Счётчик для сохранения прогресса



while True:
    count_for_save += 1
    save_bots = ''
    for i in bots:
        save_bots += str(i.brain) + '\n'

    if count_for_save == SAVE_PROGRESS:
        open('bots.txt', 'w').write(save_bots)
        count_for_save = 0

    while len(bots) > POPULATION_LEFT:
        food_left = food_count(room)
        while food_left < food:
            food_type, food_coord = create_food(ROOM_SIZE)
            while room[food_coord[0]][food_coord[1]] != ' ':
                food_type, food_coord = create_food(ROOM_SIZE)
            room[food_coord[0]][food_coord[1]] = food_type
            food_left = food_count(room)

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
            dead_count -= POPULATION_LEFT

        for d in range(dead_count):
            bots.remove(del_bots[d])

        room = relocate_bots(room, bots)
        display_array(room, score, gen_step, bots, score_best, score_last)
        score += 1

    gen_step += 1 # Обновляем номер поколения
    if score > score_best: # Обнуляем счётчик тиков лучшего поколения
        score_best = copy.deepcopy(score)
    score_last = copy.deepcopy(score)
    score = 0

    n_bots = [] # Инициализируем список с новыми ботами
    bots = change_amount(bots)
    for nn in range(POPULATION_LEFT): # Возведение с степень POPULATION_LEFT
        n_bots += generation([0,0], bots[nn].hp, bots[nn].brain, bots[nn].step, bots[nn].direction, bots[nn].make_time, nn)

    bots = generate_bots() # Создание структуры экземпляров класса
    for nn in range(POPULATION):
        bots[nn].coords, bots[nn].hp, bots[nn].brain, bots[nn].step,\
            bots[nn].direction, bots[nn].make_time = create_coord_bot(room, ROOM_SIZE), n_bots[nn][1], n_bots[nn][2], n_bots[nn][3], \
                                                    n_bots[nn][4], n_bots[nn][5]
    room = create_room(ROOM_SIZE)
    room = create_food_in_room(room, ROOM_SIZE)
    room = relocate_bots(room, bots)
    food = food_count(room)
