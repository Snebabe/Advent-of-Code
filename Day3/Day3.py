
with open("Day3\Day3input") as f:
    data = f.read()
    data = data.splitlines()

sum = 0

for value in data:
    comp1 = value[0:int(len(value)/2)]
    comp2 = value[int(len(value)/2):]

    identical = ''.join(set(comp1).intersection(comp2))
    if identical.isupper(): letterValue = ord(identical) -38
    else: letterValue = ord(identical) -96
    sum += letterValue

print(sum)
sum = 0

for index, value in enumerate(data):
    if index % 3 == 0: g1 = value
    elif index % 3 == 1: g2 = value
    elif index % 3 == 2: 
        g3 = value
        identical = ''.join(set(g1).intersection(g2, g3))
        if identical.isupper(): letterValue = ord(identical) -38
        else: letterValue = ord(identical) -96
        sum += identical

print(sum)
