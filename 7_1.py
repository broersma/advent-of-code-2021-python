import little_helper

input = list(map(int, little_helper.get_input(7, 2021).split(",")))

fuel_usage = 99999999999999999
for target_position in range(min(input), max(input)+1):
    fuel_usage = min(fuel_usage, sum(abs(pos - target_position) for pos in input))

print(fuel_usage)
