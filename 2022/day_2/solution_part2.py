"""
advent of code - day 2, part 2
"""

total_score = 0

with open("strategy_list.txt", encoding="utf-8") as strategy_list:
    for strategy in strategy_list.readlines():
        round_score = 0

        elf_move = strategy.split(" ")[0]  # elf moves
        my_move = strategy.split(" ")[1].rstrip("\n")  # my moves

        if elf_move == "A":  # rock
            if my_move == "X":  # lose
                round_score += 3  # scissors

            elif my_move == "Y":  # draw
                round_score += 4  # rock and draw

            else:  # win (z)
                round_score += 8  # paper and win

        elif elf_move == "B":  # paper
            if my_move == "X":  # lose
                round_score += 1  # rock and lose

            elif my_move == "Y":  # draw
                round_score += 5  # paper and draw

            else:  # win (z)
                round_score += 9  # scissors and win

        else:  # scissors
            if my_move == "X":  # lose
                round_score += 2  # paper

            elif my_move == "Y":  # draw
                round_score += 6  # scissors and drae

            else:  # win (z)
                round_score += 7  # win and rock

        total_score += round_score

print(
    "Following the Elf's instructions for the second"
    " column, what would your total score be if"
    " everything goes exactly according to your"
    f" strategy guide? It would be {total_score}"
)
