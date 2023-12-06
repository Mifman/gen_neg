import random as rdm
from gen_const import *
from gen_room import *

# Bot = [[Координаты], здоровье, [мозг], шаг, направление, ходов]
class Bot:
    def __init__(self, coords, hp, brain, step, direction, make_time, room):
        self.coords = create_coord_bot(room, ROOM_SIZE)
        self.hp = BOT_HP
        self.brain = create_brain()
        self.step = 0
        self.direction = rdm.randint(24,31)
        self.make_time = 0 # Даёт понять, сколько раз произошло действие

def create_brain(): # Создание мозга бота
    br = []
    for i in range(64):
        br.append(rdm.randint(0, 63))
    return br

def create_coord_bot(r, generate_room): # Генерация координат для бота
    coord = [rdm.randint(1, generate_room - 2), rdm.randint(1, generate_room - 2)]
    while r[coord[0]][coord[1]] == '#' or r[coord[0]][coord[1]] == '@':
        coord = [rdm.randint(1, generate_room - 2), rdm.randint(1, generate_room - 2)]
    return coord

def create_bot():
    return Bot(create_coord_bot(room, ROOM_SIZE), BOT_HP, create_brain(), 0, rdm.randint(24,31), 0, room)