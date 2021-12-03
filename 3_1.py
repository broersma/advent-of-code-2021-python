import little_helper

entries = little_helper.get_input(3, 2021).split()

g = [0] * 12
for entry in entries:
    num = [(1 if x == '1' else -1) for x in entry]

    for i,b in enumerate(num):
        g[i] += b

gamma = ['0' if x < 0 else '1' for x in g]
epsilon = ['0' if x > 0 else '1' for x in g]

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

print(gamma*epsilon)
