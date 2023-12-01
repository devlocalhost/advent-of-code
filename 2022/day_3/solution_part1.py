"""
advent of code - day 3, part 1
"""

lowercase_lett = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
]
uppercase_lett = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
]
sum_total = []

with open("rucksack_list.txt", encoding="utf-8") as rucksack_list:
    ruck_list = rucksack_list.readlines()

    for rucksack in enumerate(ruck_list):
        half1 = set(ruck_list[rucksack[0]][:len(ruck_list[rucksack[0]]) // 2])
        half2 = set(ruck_list[rucksack[0]][len(ruck_list[rucksack[0]]) // 2:])

        if half1 & half2:
            sharing_item = half1 & half2
            sharing_item = sharing_item.pop()

        if sharing_item in lowercase_lett:
            sum_total.append(lowercase_lett.index(sharing_item) + 1)

        else:
            sum_total.append(uppercase_lett.index(sharing_item) + 27)

    print(
        "[Part 1] Find the item type that appears in both compartments of each rucksack."
        f"What is the sum of the priorities of those item types? Its {sum(sum_total)}"
    )
