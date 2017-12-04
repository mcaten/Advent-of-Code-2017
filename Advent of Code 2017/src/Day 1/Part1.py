with open("data.txt") as f:
  data = f.readlines()

count = 0

for i in range(0, len(data[0]) - 1):
  if data[0][i] == data[0][i + 1]:
    count += int(data[0][i])
    
if data[0][0] == data[0][len(data[0]) - 1]:
  count += int(data[0][0])
    
print("Part 1 Solution:", count)