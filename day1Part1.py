import re

readFile = open("adventOfCode1.txt", "r") # open file to scan
total = 0 # initialize total which will be the sum of all numbers
digits = [] # initialize digits which will temporarily hold the digits in each line


# loop through each line of the file, if there are digits in the line, add the first and last digit to the total
for line in readFile: 
    digits = re.findall(r'\d', line) # use regex to find all digits in the line
    if digits:
        total += int((digits[0]) + (digits[-1]))

print(total) # print the total

