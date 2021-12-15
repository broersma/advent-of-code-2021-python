import little_helper

input = little_helper.get_input(14, 2021).split("\n\n")

pt = input[0]

pi = dict(tuple(line.split(" -> ")) for line in input[1].split("\n"))

for i in range(10):
    new_pt = pt[0]
    for pair in zip(pt, pt[1:]):
        pair = ''.join(pair)
        if pair in pi:
            new_pt += pi[pair] + pair[1]
    pt = new_pt

most_common = max(set(c for c in pt), key=lambda c: pt.count(c))
least_common = min(set(c for c in pt), key=lambda c: pt.count(c))
print(pt.count(most_common) - pt.count(least_common))
