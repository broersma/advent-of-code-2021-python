import little_helper

entries = little_helper.get_input(2, 2021).split()

pos = 0
depth = 0
aim = 0
for entry in zip(entries[::2], entries[1::2]):
    dir = entry[0][0]
    if dir == 'f':
        pos += int(entry[1])
        depth += int(entry[1]) * aim
    elif dir == 'u':
        aim -= int(entry[1])
    else:
        aim += int(entry[1])

print(pos*depth)
