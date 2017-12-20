with open("data.txt") as f:
  data = f.readlines()
  
balance = {}
names = []

for line in data:
  line = line.rstrip()
  arr = line.split(" ")
  towers = []
  
  if '->' in arr:
    for element in arr[3:]:
      element = element.replace(',', '')
      towers.append(element)
  
  balance[arr[0]] = towers
  names.append(arr[0])
  
for name in names:
  found = False
  for value in balance.values():
    if name in value:
      found = True
      
  if not found:
    print("Part 1 Solution:", name)