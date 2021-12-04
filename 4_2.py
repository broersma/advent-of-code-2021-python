import little_helper

input = list(little_helper.get_input(4, 2021).split("\n\n"))

numbers = list(input[0].split(","))

boards = [[row.split() for row in board.split("\n")] for board in input[1:]]

def remove_numbers(board, numbers):
    cleaned_board = []
    for row in board:
        cleaned_board.append([number for number in row if number not in numbers])
    return cleaned_board

def board_wins(board, numbers):

    transpose = map(list, zip(*board))

    cleaned_board = remove_numbers(board, numbers)
    cleaned_transpose =  remove_numbers(transpose, numbers)

    return any(len(row) == 0 for row in cleaned_board) or any(len(row) == 0 for row in cleaned_transpose)

def calculate_score(board, numbers):
    cleaned_board = remove_numbers(board, numbers)
    
    return sum(sum(int(num) for num in row) for row in cleaned_board)
        

for i in range(len(numbers)):
    available_numbers = numbers[:i + 1]

    for board in boards:
        if board_wins(board, available_numbers):
            boards.remove(board)
            if len(boards) == 0:
                print(calculate_score(board, available_numbers) * int(available_numbers[-1]))
                exit()
