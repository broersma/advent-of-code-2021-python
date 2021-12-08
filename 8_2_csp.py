from constraint import *

def solve_line(input_digits, output_digits):
    """
    >>> solve_line(["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"], ["cdfeb", "fcadb", "cdfeb", "cdbaf"])
    5353
    """
    problem = Problem()

    problem.addVariables(["a","b","c","d","e","f","g"], ["a","b","c","d","e","f","g"])

    digits = input_digits

    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(lambda a, b, c, d, e, f, g: all(a not in digit and
                                                          b not in digit and
                                                          c in digit and
                                                          d not in digit and
                                                          e not in digit and
                                                          f in digit and
                                                          g not in digit for digit in digits if len(digit) == 2))
    problem.addConstraint(lambda a, b, c, d, e, f, g: all(a in digit and
                                                          b not in digit and
                                                          c in digit and
                                                          d not in digit and
                                                          e not in digit and
                                                          f in digit and
                                                          g not in digit for digit in digits if len(digit) == 3))
    problem.addConstraint(lambda a, b, c, d, e, f, g: all(a not in digit and
                                                          b in digit and
                                                          c in digit and
                                                          d in digit and
                                                          e not in digit and
                                                          f in digit and
                                                          g not in digit for digit in digits if len(digit) == 4))
    problem.addConstraint(lambda a, d, g: all(a in digit and
                                                          d in digit and
                                                          g in digit for digit in digits if len(digit) == 5),
                                                          ("a", "d", "g"))
    problem.addConstraint(lambda a, f, g: all(a in digit and
                                                          f in digit and
                                                          g in digit for digit in digits if len(digit) == 6),
                                                          ("a", "f", "g"))

    solution = problem.getSolutions()[0]

    translation = str.maketrans({a: b for b, a in solution.items()})
    
    digit_to_num = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6,  "acf": 7, "abcdefg": 8,  "abcdfg": 9}

    def translate(digit):
        digit = digit.translate(translation)
        digit = ''.join(sorted(digit))
        return digit_to_num[digit]

    return int(''.join(str(translate(digit)) for digit in output_digits))

if __name__=='__main__':
    import little_helper
    
    input = (list(element.split(" ") for element in line.split(" | ")) for line in little_helper.get_input(8, 2021).split("\n"))

    print(sum(solve_line(line[0], line[1]) for line in input))
