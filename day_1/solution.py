"""
adventure of code - day 1
"""

calories_sum_list, elfs_calories = [], []

with open("calories_list.txt", encoding="utf-8") as calories_data:
    one_elf = []

    for line in calories_data:
        if line == "\n":
            elfs_calories.append(one_elf)
            one_elf = []

        else:
            one_elf.append(line.strip())

    elfs_calories.append(one_elf)

for elf in elfs_calories:
    elf_max_calories = 0

    for calorie in elf:
        elf_max_calories += int(calorie)
        calories_sum_list.append(elf_max_calories)

calories_sum_list.sort(reverse=True)

print(
    f"[Part 1] How many total Calories "
    "is that Elf carrying? Its carrying "
    f"{calories_sum_list[0]} calories"
)

print(
    f"[Part 2] How many Calories are those "
    "Elves carrying in total? Theyre carrying "
    f"{sum(calories_sum_list[:3])} calories"
)
