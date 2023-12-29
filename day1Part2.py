import re

readFile = open("adventOfCode1.txt", "r")

def get_digit(d):
    if d.isnumeric():
        return d
    return str(numdict.index(d))

total = 0
numdict = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

for line in readFile:
    digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line )
    if digits:
        total += int(get_digit(digits[0]) + get_digit(digits[-1]))

print(total)
