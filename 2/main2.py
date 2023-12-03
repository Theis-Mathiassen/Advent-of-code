import re

least_red = 0
least_green = 0
least_blue = 0


with open('2/input.txt') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        game_str, game_draws_str = line.split(":")
        game = int(re.findall(r'\d+', game_str)[0])
        game_draws_str = game_draws_str.split(';')
        least_red = 0
        least_green = 0
        least_blue = 0
        for draws_str in game_draws_str:
            colors = draws_str.split(',')
            for color in colors:
                if (color.find("green") != -1):
                    number = int(re.findall(r'\d+', color)[0])
                    least_green = number if number > least_green else least_green
                if (color.find("red") != -1):
                    number = int(re.findall(r'\d+', color)[0])
                    least_red = number if number > least_red else least_red
                if (color.find("blue") != -1):
                    number = int(re.findall(r'\d+', color)[0])
                    least_blue = number if number > least_blue else least_blue
        
        total += least_green * least_red * least_blue
    print(total)
