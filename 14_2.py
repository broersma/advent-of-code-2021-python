import little_helper
from collections import defaultdict

input = little_helper.get_input(14, 2021).split("\n\n")

pt = input[0]

pi = dict(tuple(line.split(" -> ")) for line in input[1].split("\n"))

counts = defaultdict(int, {''.join(pair): pt.count(''.join(pair)) for pair in zip(pt, pt[1:])})

for i in range(40):
    new_counts = defaultdict(int)
    for pair in pi:
        new_counts[pair[0] + pi[pair]] += counts[pair]
        new_counts[pi[pair] + pair[1]] += counts[pair]
    counts = new_counts

letter_count = defaultdict(int, {pt[0]:1})
for pair in counts:
    letter_count[pair[1]] += counts[pair]

print(max(letter_count.values()) - min(letter_count.values()))
