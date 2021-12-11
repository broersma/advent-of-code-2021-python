import little_helper

input = list(list(int(level) for level in list(line)) for line in little_helper.get_input(11, 2021).split("\n"))


def step(input):
    need_to_flash = False

    flashed_this_step = set()

    for y in range(10):
        for x in range(10):
            input[y][x] += 1
            if input[y][x] > 9:
                need_to_flash = True

    while need_to_flash:
        need_to_flash = False
        for y in range(10):
            for x in range(10):
                if input[y][x] > 9 and not (x,y) in flashed_this_step:
                    flashed_this_step.add((x,y))
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if not (dx, dy) == (0,0):
                                if 0 <= y + dy < 10 and 0 <= x + dx < 10:
                                    input[y+dy][x+dx] += 1
                                    if input[y+dy][x+dx] > 9 and not (x+dx, y+dy) in flashed_this_step:
                                        need_to_flash = True

    for (x,y) in flashed_this_step:
        input[y][x] = 0

    return len(flashed_this_step)


total_flashes = 0
for i in range(100):
    total_flashes += step(input)

print(total_flashes)
