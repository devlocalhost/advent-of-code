limits = {"red": 12, "green": 13, "blue": 14}
valid_games = []

with open("input.txt", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        game_id = line.split(":")[0].split(" ")[1]
        cubes = [i.strip() for i in line.split(":")[1].strip().split(";")]

        cubes_len = 0
        invalid_cubes = 0

        for cubes_list in cubes:
            cubes_len += 1

            for i in cubes_list.split(", "):
                cube_color = i.split(" ")[1]
                cube_count = int(i.split(" ")[0])

                cube_color_limit = limits[cube_color]

                if cube_count <= limits[cube_color]:
                    print(f" --- GAME {game_id}                 VALID --- ")

                else:
                    print(f" --- GAME {game_id}             NOT VALID --- ")
                    invalid_cubes += 1

        if invalid_cubes == 0:
            valid_games.append(int(game_id))

print(sum(valid_games))
