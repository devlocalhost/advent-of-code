limits = {"red": 12, "green": 13, "blue": 14}
valid_games = []

with open("input.txt", encoding="utf-8") as file:
    for line in file.readlines():
        game_id = line.split(":")[0].split(" ")[1]
        cubes = [i.strip() for i in line.split(":")[1].strip().split(";")]

        invalid_cubes = 0

        for cubes_list in cubes:
            for i in cubes_list.split(", "):
                cube_color = i.split(" ")[1]
                cube_count = int(i.split(" ")[0])

                if cube_count > limits[cube_color]:
                    invalid_cubes += 1

        if invalid_cubes == 0:
            valid_games.append(int(game_id))

print(sum(valid_games))
