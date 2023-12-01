"""
advent of code - day 2, part 1
"""

total_score = 0

with open("strategy_list.txt", encoding="utf-8") as strategy_list:
    for strategy in strategy_list.readlines():
        round_score = 0

        elf_move = strategy.split(" ")[0]  # elf moves
        my_move = strategy.split(" ")[1].rstrip("\n")  # my moves

        if elf_move == "A":  # rock
            if my_move == "X":  # rock
                round_score += 4  # 1 for choice, 3 for draw

            elif my_move == "Y":  # paper
                round_score += 8  # 2 for choice, 6 for win

            else:  # scissors
                round_score += 3  # 3 for choice, 0 for lose

        elif elf_move == "B":  # paper
            if my_move == "X":  # rock
                round_score += 1  # 1 for choice, 0 for lose

            elif my_move == "Y":  # paper
                round_score += 5  # 2 for choice, 3 for draw

            else:  # scissors
                round_score += 9  # 3 for choice, 6 for win

        else:  # scissors
            if my_move == "X":  # rock
                round_score += 7  # 1 for choice, 6 for win

            elif my_move == "Y":  # paper
                round_score += 2  # 2 for choice, 0 for lose

            else:  # scissors
                round_score += 6  # 3 for choice, 3 for draw

        total_score += round_score

print(
    "What would your total score be if everything"
    " goes exactly according to your strategy guide?"
    f" It would be {total_score}"
)
