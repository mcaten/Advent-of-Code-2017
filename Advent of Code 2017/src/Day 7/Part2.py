from anytree import Node, RenderTree
with open("data.txt") as f:
    data = f.readlines()

nodes = []
class Disk:
    parent = ""
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children


disks = {}
balance = {}
pc = {}
names = []

for line in data:
    line = line.rstrip()
    arr = line.split(" ")
    names.append(arr[0])
    towers = []

    if '->' in arr:
        for element in arr[3:]:
            element = element.replace(',', '')
            towers.append(element)
            pc[element] = arr[0]

    balance[arr[0]] = towers
    disks[arr[0]] = (Disk(arr[0], int(arr[1][1:len(arr[1]) - 1]), towers))

first = ""
for name in names:
    found = False
    for value in balance.values():
        if name in value:
            found = True

    if not found:
        first = name
nodes = {}
base = Node(first)
nodes[first] = base

while len(pc) > 0:
    name = ""
    par = ""
    for child in pc:
        if pc[child] in nodes:
            name = child
            par = pc[child]

    nodes[name] = Node(name, parent=nodes[par])
    del pc[name]

for pre, fill, node in RenderTree(base):
    print("%s%s" % (pre, node.name))