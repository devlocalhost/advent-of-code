"""
advent of code - day 5
"""

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

with open("supply_stacks.txt", encoding="utf-8") as data:
    supply_stacks = data.readlines()

    supplies = []

    for stack in zip(*supply_stacks[:9]):
        if stack[-1:][0] in nums:
            supplies.append([stack for stack in stack if stack != " "])

    for move in supply_stacks[10:]:
        instruction = move.split("move ").pop().split(" from")

        item = int(instruction[0])

        move_instruction = instruction[1].split("to ")

        old_place = int(move_instruction[0].strip().rstrip())
        new_place = int(move_instruction[1].rstrip())

        print(old_place, "->", new_place)
        print("old", supplies[old_place - 1])

        supplies[new_place - 1].insert(0, supplies[old_place - 1][item - 1])
        supplies[old_place - 1].pop(item - 1)

        print("old", supplies[old_place - 1])
        print("new", supplies[new_place - 1])
