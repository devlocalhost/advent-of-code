"""
advent of code - day 4, part 1
"""

count = 0

with open("assignments.txt", encoding="utf-8") as assignments:
    for assignment in assignments.readlines():
        data = assignment.rstrip()

        format_data = [x.split("-") for x in data.split(",")]
        list1, list2 = [int(b) for b in format_data[0]], [
            int(c) for c in format_data[1]
        ]

        check_range = range(int(list1[0]), int(list1[1]) + 1)

        if int(list2[0]) and int(list2[1]) in check_range:
            count += 1

print(
    "[Part 1] In how many assignment pairs does one "
    f"range fully contain the other? In {count} pairs"
)
