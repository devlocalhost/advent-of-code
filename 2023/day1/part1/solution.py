numbers = []

with open("input.txt", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        line_numbers = []

        for letter in line:
            if letter.isdigit():
                line_numbers.append(int(letter))

        # lol...
        number = f"{line_numbers[0]}{line_numbers[-1:][0]}"

        numbers.append(int(number))

print(sum(numbers))
