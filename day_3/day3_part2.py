"""
advent of code - day 3, part 2
"""

from itertools import islice

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
    while True:
        iter_slice = list(islice(rucksack_list, 3))

        try:
            ruck1 = set(iter_slice[0])
            ruck2 = set(iter_slice[1])
            ruck3 = set(iter_slice[2])

            result = ruck1 & ruck2 & ruck3
            sharing_item = "".join(result).replace("\n", "")

        except IndexError:
            pass

        if not iter_slice:
            break

        if sharing_item in lowercase_lett:
            sum_total.append(lowercase_lett.index(sharing_item) + 1)

        else:
            sum_total.append(uppercase_lett.index(sharing_item) + 27)

    print(
        "[Part 2] Find the item type that appears in both compartments of each rucksack. "
        f"What is the sum of the priorities of those item types? Its {sum(sum_total)}"
    )
