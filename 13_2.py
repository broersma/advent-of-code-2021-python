import little_helper

input = little_helper.get_input(13, 2021).split("\n\n")

dots = set(tuple(map(int, line.split(","))) for line in input[0].split("\n"))

instructions = (((splitted := line[11:].split("="))[0], int(splitted[1])) for line in input[1].split("\n"))

for i in instructions:
    folded_dots = set()
    for dot in dots:
        if i[0] == "x":
            if dot[0] > i[1]:
                folded_dots.add((i[1] - (dot[0] - i[1]), dot[1]))
            else:
                folded_dots.add(dot)
        elif i[0] == "y":
            if dot[1] > i[1]:
                folded_dots.add((dot[0], i[1] - (dot[1] - i[1])))
            else:
                folded_dots.add(dot)
    dots = folded_dots

for y in range(6):
    for x in range(39):
        if (x,y) in dots:
            print("#", end='')
        else:
            print(".", end='')
    print()
