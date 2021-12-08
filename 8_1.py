import little_helper
input = ((element.split(" ") for element in line.split(" | ")) for line in little_helper.get_input(8, 2021).split("\n"))

count = 0
for line in input:
    i, o = line
    for digit in o:
        if len(digit) in [2, 4, 3, 7]:
            count += 1

print(count)