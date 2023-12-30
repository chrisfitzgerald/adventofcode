import re
import numpy as np

readFile = open('day2.txt', 'r')
#games = '''
#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#'''
#

def colorCounter (str):
    for lines in str:
        color_counts = re.findall(r'(\d+) (blue|red|green)', lines)
        counts = {}
        for count, color in color_counts:
            counts[color] = counts.get(color, 0) + int(count)
    print(counts)


#def gameCounter (str):
#    for line in str:
#        game_counts = re.findall(r'(Game) (\d+)', str )
#        print(game_counts)
#

#gameCounter(games)
colorCounter(readFile)

#for line in games.split('\n'):
#    if re.findall(r'([0-9]{1,2})blue|red|green', line):
#        print(line)