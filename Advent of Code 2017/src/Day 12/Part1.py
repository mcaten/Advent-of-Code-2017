with open('data.txt') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].rstrip()


class Pipe:
    def __init__(self, id, children):
        self.id  = id
        self.children = children

    def add_child(self, pipe):
        self.children.append(pipe)


pipes = {}
for element in data:
    li = element.split(" ")
    pipes[int(li[0])] = Pipe(int(li[0]), [])

for element in data:
    li = element.split(" ")
    for child in li[2:]:
        pipes[int(li[0])].add_child(pipes[int(child.rstrip(','))])

used = []


def can_talk(pipe, used):
    for ch in pipe.children:
        if ch.id not in used:
            used.append(ch.id)
            can_talk(ch, used)


can_talk(pipes[0], used)
print("Part 1 Solution:", len(used))