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

"""with open("day5_input.txt", "r") as file:
    full_txt = [line.strip() for line in file.readlines()]

print(full_txt)"""


def read_rules_and_updates(filename):
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    
    rules = []
    updates = []
    for line in lines:
        if '|' in line:
            rules.append(tuple(map(int, line.split('|'))))
        else:
            updates.append(list(map(int, line.split(','))))

    return rules, updates

def satisfies_rules(update, rules):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def central_number(lst):
    n = len(lst)
    return lst[n // 2] if n % 2 == 1 else lst[(n // 2) - 1]

def sum_central_numbers(filename):
    rules, updates = read_rules_and_updates(filename)
    central_sum = 0
    
    for update in updates:
        if satisfies_rules(update, rules):
            central_sum += central_number(update)
    
    return central_sum

# Example usage
filename = "day5_input.txt"
result = sum_central_numbers(filename)
print(result)
