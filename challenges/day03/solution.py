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

import re

with open("day3_input.txt", "r") as file:
    full_txt = file.read()

# Part 1.

pattern = r"mul\(\d+,\d+\)"
num_pattern = r"\d+"

matches = re.findall(pattern, full_txt)

total_sum = 0

for match in matches:
    match = re.findall(num_pattern, match)
    num1, num2 = map(int, match)
    total_sum += num1 * num2

# print(total_sum)

# Part 2.

counting = True
result = 0

for line in full_txt.splitlines():
    parts = re.split(r"(do\(\)|don't\(\))", line)
    for part in parts:
        if part == "do()":
            counting = True
        elif part == "don't()":
            counting = False
        elif counting:
            matches = re.findall(pattern, part)
            for match in matches:
                numbers = re.findall(num_pattern, match)
                num1, num2 = map(int, numbers)
                result += num1 * num2

# print(result)
