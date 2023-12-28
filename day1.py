import re

readFile = open("adventOfCode1.txt", "r")
total = 0
numdict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,}

for line in readFile:
    digits = [char for char in line if char.isdigit()]
    words = re.findall(r'(?:one|two|three|four|five|six|seven|eight|nine)', line, flags=re.IGNORECASE)
    if digits:
        concatenated_digits = str(digits[0]) + str(digits[-1])
        total += int(concatenated_digits)
    else:
        num = numdict.get(words[0].lower())
        total += num

print(total)
