"""
.--------------------------------------------------------------------------------------------------------------------.
|                                                                                                                    |
|                                                                                                                    |
|                                                                                                                    |
|    █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗     ██████╗ ███████╗     ██████╗ ██████╗ ██████╗ ███████╗   |
|   ██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝    ██╔═══██╗██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝   |
|   ███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║       ██║   ██║█████╗      ██║     ██║   ██║██║  ██║█████╗     |
|   ██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║       ██║   ██║██╔══╝      ██║     ██║   ██║██║  ██║██╔══╝     |
|   ██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║       ╚██████╔╝██║         ╚██████╗╚██████╔╝██████╔╝███████╗   |
|   ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝        ╚═════╝ ╚═╝          ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝   |
|                                                                                                                    |
|                                       ██████╗  ██████╗ ██████╗ ██╗  ██╗                                            |
|                                       ╚════██╗██╔═████╗╚════██╗██║  ██║                                            |
|                                        █████╔╝██║██╔██║ █████╔╝███████║                                            |
|                                       ██╔═══╝ ████╔╝██║██╔═══╝ ╚════██║                                            |
|                                       ███████╗╚██████╔╝███████╗     ██║                                            |
|                                       ╚══════╝ ╚═════╝ ╚══════╝     ╚═╝                                            |
|                                                                                                                    |
|                                             42_user: antonimo                                                      |
|                                             github: antonimodev                                                    |
|                                                                                                                    |
'--------------------------------------------------------------------------------------------------------------------'
"""

# Part 1.

def is_word_in_direction(
    matrix: list[list], 
    word: str, 
    start_row: int, 
    start_col: int, 
    row_step: int, 
    col_step: int
) -> bool:

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(len(word)):
        new_row = start_row + row_step * i
        new_col = start_col + col_step * i

        if new_row < 0 or new_row >= rows:
            return False
        elif new_col < 0 or new_col >= cols:
            return False
        elif matrix[new_row][new_col] != word[i]:
            return False

    return True


def count_words(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    total_count = 0

    # NOTE: Directions equivalent to right, down, down right, down left
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for row in range(rows):
        for col in range(cols):
            for row_step, col_step in directions:
                if is_word_in_direction(matrix, word, row, col, row_step, col_step):
                    total_count += 1
                if is_word_in_direction(matrix, word, row, col, -row_step, -col_step):
                    total_count += 1

    return total_count


with open("day4_input.txt", "r") as file:
    matrix = [line.strip() for line in file.readlines()]

count = count_words(matrix, "XMAS")

print(count)
