with open('data.txt') as f:
  data = f.readlines()
  
def no_duplicates(str):
  str = str.rstrip()
  split = str.split(' ')
  dict = {}
  
  for val in split:
    if val in dict:
      return False
    
    else:
      dict[val] = 1
  return True
 
count = 0 
for item in data:
  if no_duplicates(item):
    count +=1 
    
print("Part 1 Solution:", count)