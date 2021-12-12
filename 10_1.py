import little_helper

input = little_helper.get_input(10, 2021).split("\n")

score = 0

for line in input:
    stack = []
    for i, c in enumerate(line):
        if c in "([{<":
            stack.append(c)
        else:
            l = stack[-1]
            if l+c == "()" or l+c == "[]" or l+c == "{}" or l+c == "<>":
                stack.pop()
            else:
                if c == ")":
                    score += 3
                elif c == "]":
                    score += 57
                elif c == "}":
                    score += 1197
                elif c == ">":
                    score += 25137
                break

print(score
