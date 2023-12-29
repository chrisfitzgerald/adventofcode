import re

readFile = open("adventOfCode1.txt", "r")
total = 0

for line in readFile:
    digits = re.findall(r'\d', line)
    if digits:
        concatenated_number = int(digits[0]) + int(digits[-1])
        total += concatenated_number

print(total)