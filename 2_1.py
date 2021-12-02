import little_helper

entries = little_helper.get_input(2, 2021).split()

pos = 0
depth = 0
for entry in zip(entries[::2], entries[1::2]):
    dir = entry[0][0]
    if dir == 'f':
        pos += int(entry[1])
    elif dir == 'u':
        depth -= int(entry[1])
    else:
        depth += int(entry[1])

print(pos*depth)
