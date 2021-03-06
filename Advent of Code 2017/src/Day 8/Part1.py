with open('data.txt') as f:
    data = f.readlines()

map = {}
for line in data:
    line = line.rstrip()
    split = line.split(" ")

    if not split[0] in map:
        map[split[0]] = 0
    if not split[4] in map:
        map[split[4]] = 0

    operation = split[1]

    boo = eval(str(map[split[4]]) + split[5] + split[6])
    if boo:
        if operation == 'inc':
            map[split[0]] += int(split[2])
        else:
            map[split[0]] -= int(split[2])

print("Part 1 Solution:", max(map.values()))