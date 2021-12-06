import little_helper

input = map(int, little_helper.get_input(6, 2021).split(","))

def process(fishes):
    for j in fishes:
        if j == 0:
            yield 6
            yield 8
        else:
            yield j-1

for i in range(80):
    input = list(process(input))

print(len(list(input)))
