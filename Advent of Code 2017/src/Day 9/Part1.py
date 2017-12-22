import re
with open('data.txt') as f:
    data = f.readlines()

text = data[0]

regex1 = '\![^"]'
text = re.sub(regex1, "", text)
regex2 = '\<.*?\>'
text = re.sub(regex2, "",  text)

depth = 0
score = 0
for letter in text:
    if letter == '{':
        depth += 1
    elif letter == '}':
        score += depth
        depth -= 1

print("Part 1 Solution:", score)