import little_helper
from functools import cache

input = list(map(int, little_helper.get_input(6, 2021).split(",")))

@cache
def get_days_left_at_spawns(individual, days_left):
    days_left -= individual + 1
    while days_left >= 0:
        yield days_left
        days_left -= 7

@cache
def num_fish(individual, days_left):
    posterity = 0
    for days_left_at_spawn in get_days_left_at_spawns(individual, days_left):
        posterity += num_fish(8, days_left_at_spawn)
    return 1 + posterity

print(sum(map(lambda f: num_fish(f, 256), input)))
