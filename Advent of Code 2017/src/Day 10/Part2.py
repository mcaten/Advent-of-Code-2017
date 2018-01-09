from functools import reduce
with open('data.txt') as f:
    inp = f.readlines()

data = []
for item in inp[0]:
    data.append(ord(item))

data += [17, 31, 73, 47, 23]

li = []
for i in range(256):
    li.append(i)

indx = 0
skip = 0

for i in range(64):
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


li = [li[i:i+16] for i in range(0, len(li), 16)]

dense = []
for arr in li:
    xor = reduce(lambda a, b: a ^ b, arr, 0)
    dense.append(xor)

fin = ""
for value in dense:
    if value < 10:
        fin += "0" + str(value)
    else:
        fin += hex(value)[2:]
        
print("Part 2 Solution:", fin)