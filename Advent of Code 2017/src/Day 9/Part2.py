import re
with open('data.txt') as f:
    data = f.readlines()

text = data[0]

in_garbage = False
skip = False
score = 0
for char in text:
    if in_garbage:
        if skip:
            skip = False
        elif char == '>':
            in_garbage = False

        elif char == '!':
            skip = True

        else:
            score += 1

    else:
        if char == '<':
            in_garbage = True

print("Part 2 Solution:", score)