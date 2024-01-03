import re

readFile = open('day2.txt', 'r')

def colorCounter (str):
    invalid_games = []
    for lines in str:
        color_counts = re.findall(r'(\d+) (blue|red|green)', lines)
        counts = {}
        for count, color in color_counts:
            #counts[color] = counts.get(color, 0) + int(count)
            if (int(count) > 12 and color == 'red') or (int(count) > 14 and color == 'blue') or (int(count) > 13 and color == 'green'):
                print(lines) #use this to debug which games are invalid
                break
    return invalid_games


def gameCounter (i):
    for line in i:
        game_counts = re.findall(r'(Game) (\d+)', line)
        for game, count in game_counts:
            count[count] = count.get(game, 0) + int(count)
        print(game_counts)

#colorCounter(readFile)
invalid_games = colorCounter(readFile)
gameCounter(invalid_games)

