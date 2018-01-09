with open('data.txt') as f:
    data = f.readlines()

data = map(int, data[0].split(','))

li = []
for i in range(256):
    li.append(i)

indx = 0
skip = 0

for element in data:
    count = indx % len(li)
    rev = []

    for i in range(element):
        rev.append(li[count])
        count += 1

        if count >= len(li):
            count = 0

    rev = rev[::-1]

    count2 = indx % len(li)
    for num in rev:
        li[count2] = num
        count2 += 1

        if count2 >= len(li):
            count2 = 0

    indx += element + skip
    skip += 1

print("Part 1 Solution:", li[0] * li[1])