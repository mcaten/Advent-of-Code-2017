import re
with open('data.txt') as f:
    data = f.readlines()

data = re.split(',', data[0])

x = 0
y = 0
for direction in data:
    if direction == 'n':
        y += 1
    elif direction == 'ne':
        x += 0.5
        y += 0.5
    elif direction == 'se':
        x += 0.5
        y -= 0.5
    elif direction == 's':
        y -= 1
    elif direction == 'sw':
        x -= 0.5
        y -= 0.5
    elif direction == 'nw':
        x -= 0.5
        y += 0.5
print("Part 1 Solution:", (int(abs(x) + abs(y))))