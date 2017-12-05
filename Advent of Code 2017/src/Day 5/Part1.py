with open('data.txt') as f:
  data = f.readlines()


for i in range(0, len(data)):
  data[i] = int(data[i].rstrip())
  
indx = 0
count = 0

while indx >= 0 and indx < len(data):
  temp = data[indx]
  data[indx] += 1
  indx += temp
  count += 1
  
print("Part 1 Solution:", count)