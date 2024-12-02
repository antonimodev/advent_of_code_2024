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

# NOTE: Part 1.


def is_valid_difference(num1: int, num2: int) -> bool:
    return 1 <= abs(num1 - num2) <= 3


# NOTE: problem_dampener is from part 2.
def problem_dampener(group: list) -> list:
    for i in range(len(group)):
        group_cpy = group[:i] + group[i + 1:]
        if is_safe_report(group_cpy):
            return group_cpy
    return group


def is_safe_report(group: list) -> bool:
    if len(group) < 2:
        return True

    if group[0] > group[1]:
        trend = "decreasing"
    elif group[0] < group[1]:
        trend = "increasing"
    else:
        return False

    for i in range(len(group) - 1):
        if not is_valid_difference(group[i], group[i + 1]):
            return False
        if trend == "decreasing" and group[i] <= group[i + 1]:
            return False
        elif trend == "increasing" and group[i] >= group[i + 1]:
            return False

    return True


with open("day2_input.txt", "r") as file:
    full_txt = file.readlines()

full_txt = [list(map(int, reports.strip("\n").split())) for reports in full_txt]

safe_reports = 0

for group in full_txt:
    if not is_safe_report(group):
        new_group = problem_dampener(group)
        if is_safe_report(new_group):
            safe_reports += 1
    else:
        safe_reports += 1

# print(safe_reports)
