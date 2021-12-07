import little_helper
from more_itertools import interleave

input = list(map(int, little_helper.get_input(7, 2021).split(",")))

fuel_usage = 99999999999999999
center_pos = sum(input) // len(input)
for target_position in interleave(range(center_pos, max(input)), range(center_pos-1, min(input), -1)):
    fuel_usage = min(fuel_usage, sum(sum(range(abs(pos - target_position)+1)) for pos in input))
    print(fuel_usage, flush=True)

print(fuel_usage)
