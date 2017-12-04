with open("data.txt") as f:
  data = f.readlines()
  
result = []

for line in data:
  l = line.split('\t')
  intlist = [int(x) for x in l]
  
  for val in range(0, len(intlist)):
    for indx in range(0, len(intlist)):
      if indx != val and intlist[val] % intlist[indx] == 0:
        result.append(intlist[val] / intlist[indx])
    
  
print("Part 2 Solution:", sum(result))