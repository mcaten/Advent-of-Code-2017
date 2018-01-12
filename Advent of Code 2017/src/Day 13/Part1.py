with open('data.txt') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].rstrip()

class Row:
    def __init__(self, length):
        self.length = length
        self.current_pos = 0
        self.direction = 'D'

    def move(self):
        if self.current_pos + 1 == self.length and self.direction == 'D':
            self.current_pos -= 1
            self.direction = 'U'

        elif self.current_pos - 1 < 0 and self.direction == 'U':
            self.current_pos += 1
            self.direction = 'D'

        elif self.direction == 'D':
            self.current_pos += 1

        elif self.direction == 'U':
            self.current_pos -= 1


sc = [0] * 93

for line in data:
    sp = line.split(" ")
    num = int(sp[0].replace(':', ''))
    sc[num] = Row(int(sp[1]))

sc_pos = -1

l = []
for i in range(92):
    sc_pos += 1

    if sc[sc_pos] != 0 and sc[sc_pos].current_pos == 0:
        l.append(sc_pos)

    for scanner in sc:
        if scanner != 0:
            #print(scanner.current_pos)
            scanner.move()

sum = 0
for num in l:
    sum += (num * sc[num].length)

print("Part 1 Solution:", sum)