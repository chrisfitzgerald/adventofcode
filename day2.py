import re

def colorCounter(file):
    validGames = 0  
    for line in file:
        color_counts = re.findall(r'(\d+) (blue|red|green)', line) 
        for count, color in color_counts:
            if (int(count) > 12 and color == 'red') or (int(count) > 14 and color == 'blue') or (int(count) > 13 and color == 'green'):
                break
        else:
            game_counts = re.findall(r'(Game) (\d+)', line)
            for game, gameNum in game_counts:
                validGames += int(gameNum)
    print("Unsatisfied Total:", validGames)

with open('day2.txt') as file:
    colorCounter(file)
