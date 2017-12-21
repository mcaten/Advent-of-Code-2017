from anytree import Node, RenderTree
with open("data.txt") as f:
    data = f.readlines()

nodes = []
class Disk:
    parent = ""
    net_weight = 0
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children


disks = {}
balance = {}
pc = {}
names = []
net = 0

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
    net += int(arr[1][1:len(arr[1]) - 1])

first = ""
for name in names:
    found = False
    for value in balance.values():
        if name in value:
            found = True

    if not found:
        first = name
nodes = {}
base = Node(first, weight=disks[first].weight)
nodes[first] = base

while len(pc) > 0:
    name = ""
    par = ""
    for child in pc:
        if pc[child] in nodes:
            name = child
            par = pc[child]

    nodes[name] = Node(name, weight=disks[name].weight, parent=nodes[par])
    del pc[name]

def calculate_sum(cur):
    children_sum = 0
    for child in cur.children:
        children_sum += calculate_sum(child)
    return cur.weight + children_sum

for key,val in nodes.items():
    disks[key].net_weight = calculate_sum(val)

for pre, fill, node in RenderTree(base):
    print("%s%s%s" % (pre, node.name, " " + str(disks[node.name].net_weight)))

def all_same(items):
    return all(x == items[0] for x in items)