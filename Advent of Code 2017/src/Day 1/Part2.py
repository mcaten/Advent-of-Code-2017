with open("data.txt") as f:
  data = f.readlines()
  
count = 0
half = len(data[0]) / 2

for i in range(0, len(data[0])):
  first = data[0][i]
  indx = int(i + half)
  
  if i + half >= len(data[0]):
    indx -= len(data[0])
  
  last = data[0][indx]
  
  if first == last:
    count += int(first)
    
print("Part 2 Solution:", count)