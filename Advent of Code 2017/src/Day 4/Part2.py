with open('data.txt') as f:
  data = f.readlines()
  
def is_valid(str):
  str = str.rstrip()
  split = str.split(' ')
  
  for indx in range(0, len(split)):
    letters = list(split[indx])
    
    for indx2 in range(0, len(split)):
      if(indx != indx2):
        letters2 = list(split[indx2])
      
        if len(letters) == len(letters2) and contains_letters(letters, letters2):
          return False
  return True 
    
def contains_letters(word, word2):
  for letter in word:
    if letter in word2:
      word2.remove(letter)
    
  if(len(word2) == 0):
    return True
    
  return False
  
sum = 0
for line in data:
  if is_valid(line):
    sum += 1

print("Part 2 Solution:", sum)