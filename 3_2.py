import little_helper

entries = little_helper.get_input(3, 2021).split()


def calculate_g_e(entries):
    g = [0] * 12
    for entry in entries:
        num = [(1 if x == '1' else -1) for x in entry]

        for i,b in enumerate(num):
            g[i] += b

    gamma = ['0' if x < 0 else '1' for x in g]
    epsilon = ['0' if x >= 0 else '1' for x in g]

    return gamma, epsilon


ox_values = entries[::]

gamma, _ = calculate_g_e(ox_values)

for i in range(12):
    ox_values = [value for value in ox_values if value[i] == gamma[i]]

    if len(ox_values) == 1:
        break

    gamma, _ = calculate_g_e(ox_values)

co2_values = entries[::]

_, epsilon = calculate_g_e(co2_values)

for i in range(12):
    co2_values = [value for value in co2_values if value[i] == epsilon[i]]

    if len(co2_values) == 1:
        break

    _, epsilon = calculate_g_e(co2_values)

ox_value = int(''.join(ox_values[0]), 2)
co2_value = int(''.join(co2_values[0]), 2)

print(ox_value*co2_value)
