input = 368078

data = []
for i in range(0, 607):
  new = []
  for i in range(0, 607):
    new.append(0)
  data.append(new)

col = 304
row = 303
picked = False
direction = 'E'
data[303][303] = 1

for val in range (2, 607 ** 2):
  count = 0
  if row > 0:
    count += data[row - 1][col]
    if col > 0:
      count += data[row - 1][col - 1]
  if row + 1 < 607:
    count += data[row + 1][col]
    if col + 1 < 607:
      count += data[row + 1][col + 1]
  if col + 1 < 607:
    count += data[row][col + 1]
    if row > 0:
      count += data[row - 1][col + 1]
  if col > 0:
    count += data[row][col - 1]
    if row + 1 < 607:
      count += data[row + 1][col - 1]
  data[row][col] = count
  
  if count > input:
    print("Part 2 Solution:", count)
    break
  
  if direction == 'E' and data[row - 1][col] == 0:
    direction = 'N'
    row -= 1
    
  elif not picked and direction == 'E':
    col += 1
    
  elif not picked and direction == 'N' and data[row][col - 1] == 0:
    direction = 'W'
    col -= 1
    
  elif not picked and direction == 'N':
    row -= 1
    
  elif not picked and direction == 'W' and data[row + 1][col] == 0:
    direction = 'S'
    row += 1
    
  elif not picked and direction == 'W':
    col -= 1
    
  elif not picked and direction == 'S' and data[row][col + 1] == 0:
    direction = 'E'
    col += 1
    
  elif not picked and direction == 'S':
    row += 1
  
def index_2d(mydata, v):
  for c, x in enumerate(mydata):
    if v in x:
      return [c, x.index(v)]

