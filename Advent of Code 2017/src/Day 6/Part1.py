with open("data.txt") as f:
  data = f.readlines()
  
for i in range(0, len(data)):
  data[i] = int(data[i].rstrip())
  
def distribute_value(list, indx):
  num = list[indx]
  list[indx] = 0
  
  while num != 0:
    indx+= 1
    if indx  == len(list):
      indx = 0
    list[indx] += 1
    num -=1
    
  
found = False
count = 1
combinations = []

while(not found):
  indx = data.index(max(data))
  distribute_value(data, indx)
  
  if not data in combinations:
    copy = list(data)
    combinations.append(copy)
  else:
    print("Part 1 Solution:", count)
    found = True
  count += 1

