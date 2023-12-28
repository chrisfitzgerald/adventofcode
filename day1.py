readFile = open("adventOfCode1.txt", "r")
total = 0

for line in readFile:
    digits = [char for char in line if char.isdigit()]
    if digits:
        concatenated_digits = str(digits[0]) + str(digits[-1])
        total += int(concatenated_digits)

print(total)
