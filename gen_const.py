


ROOM_SIZE = 45 # Размер Комнаты

#######################
# Должно быть рассчитано так, чтобы POPULATION_LEFT ** 2 == POPULATION

POPULATION = 64 # Начальная популяция
POPULATION_LEFT = 8 # До какого момента происходит смена популяции
#######################

BOT_HP = 35 # Сколько хп у бота на старте

BOT_HP_MAX = 80 # Максимальное хп у бота

EAT_INCREMENT = 10 # Прибавка к здоровью бота за еду

POISON_DAMAGE = 100 # Урон от съедения яда

MAKE_TIME_MAX = 10 # Максимум ходов бота за тик

MAX_MUTATION = 8 # Максимум мутантов (минимум 1)

MAX_MUTATION_BOT = 8 # Максимум мутаций в гене (минимум 1)

CREATE_FOOD_TICK = 1 # Сколько тиков должно пройти, прежде чем создать единицу пищи

LIST_EL = ['*', '*', '&', '*'] + ([' '] * 20) # Список для генерации комнаты