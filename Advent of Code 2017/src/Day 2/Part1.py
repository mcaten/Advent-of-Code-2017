with open("data.txt") as f:
  data = f.readlines()
  
difference = []

for line in data:
  l = line.split('\t')
  intlist = [int(x) for x in l]
  
  mi = min(intlist)
  ma = max(intlist)
  
  difference.append(ma - mi)
  
print("Part 1 Solution:", sum(difference))