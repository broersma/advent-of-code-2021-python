import little_helper

input = little_helper.get_input(10, 2021).split("\n")

scores = []

for line in input:
    stack = []
    corrupt = False
    for i, c in enumerate(line):
        if c in "([{<":
            stack.append(c)
        else:
            l = stack[-1]
            if l+c == "()" or l+c == "[]" or l+c == "{}" or l+c == "<>":
                stack.pop()
            else:
                corrupt = True
                break
    if not corrupt:
        score = 0
        points = {"(": 1, "[": 2, "{": 3, "<": 4}
        for c in stack[::-1]:
            score *= 5
            score += points[c]
        scores.append(score)

print(sorted(scores)[len(scores)//2])
