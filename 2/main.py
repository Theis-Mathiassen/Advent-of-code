import re

max_red = 12
max_green = 13
max_blue = 14


with open('2/input.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        game_str, game_draws_str = line.split(":")
        game = int(re.findall(r'\d+', game_str)[0])
        game_draws_str = game_draws_str.split(';')
        game_allowed = True
        for draws_str in game_draws_str:
            colors = draws_str.split(',')
            for color in colors:
                if (color.find("green") != -1):
                    number = int(re.findall(r'\d+', color)[0])
                    game_allowed = False if number > max_green else game_allowed
                if (color.find("red") != -1):
                    number = int(re.findall(r'\d+', color)[0])
                    game_allowed = False if number > max_red else game_allowed
                if (color.find("blue") != -1):
                    number = int(re.findall(r'\d+', color)[0])
                    game_allowed = False if number > max_blue else game_allowed
        
        if game_allowed:
            total += game
    print(total)
