from collections import defaultdict
import little_helper

input = ((element.split(" ") for element in line.split(" | ")) for line in little_helper.get_input(8, 2021).split("\n"))


def to_set(digit_str):
    digit_set = set()
    for c in digit_str:
        digit_set.add(c)
    return digit_set


count = 0

for line in input:
    i, o = line

    code = defaultdict(set)
    for digit in i:
        len_digit = len(digit)
        digit_set = to_set(digit)
        if len_digit == 2:
            code[1] = digit_set
        elif len_digit == 3:
            code[7] = digit_set
        elif len_digit == 4:
            code[4] = digit_set
        elif len_digit == 7:
            code[8] = digit_set

    for digit in i:
        len_digit = len(digit)
        digit_set = to_set(digit)
        if len_digit == 6:
            len_intersection = len(code[1].intersection(digit_set))
            if len_intersection == 1:
                code[6] = digit_set
            else:
                len_intersection = len((code[4] - code[1]).intersection(digit_set))
                if len_intersection == 1:
                    code[0] = digit_set
                else:
                    code[9] = digit_set

    for digit in i:
        len_digit = len(digit)
        digit_set = to_set(digit)
        if len_digit == 5:
            len_intersection = len(code[6].intersection(digit_set))
            if len_intersection == 5:
                code[5] = digit_set
            else:
                len_intersection = len(code[4].intersection(digit_set))
                if len_intersection == 2:
                    code[2] = digit_set
                else:
                    code[3] = digit_set

    code2 = {}
    for k in code:
        code2[''.join(sorted(code[k]))] = k

    count += int(''.join(str(code2[''.join(sorted(digit))]) for digit in o))

print(count)