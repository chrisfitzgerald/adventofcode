import re

sampleGames = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.split('\n')


def CubeCounter(data):
    total = 0
    for line in data:
        color_counts = re.findall(r'(\d+) (blue|red|green)', line) 
        max_red = 0
        max_blue = 0
        max_green = 0
        for count, color in color_counts:
            if color == 'red':
                max_red = max(max_red, int(count))
            elif color == 'blue':
                max_blue = max(max_blue, int(count))
            elif color == 'green':
                max_green = max(max_green, int(count)) 
        total = total + (max_red * max_blue * max_green)
    print(total)
               
#CubeCounter(sampleGames)
with open('day2.txt') as file:
    CubeCounter(file)
