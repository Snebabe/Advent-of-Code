with open("Day2\Day2input") as f:
    data = f.read()
    data = data.splitlines()

score = 0

for item in data:
    if item[0] == "A":  #rock
        if item[2] == "X":
            score += 3
        elif item[2] == "Y":
            score += 4
        else:
            score += 8

    elif item[0] == "B":  #paper
        if item[2] == "X":
            score += 1
        elif item[2] == "Y":
            score += 5
        else:
            score += 9
    else:                 #sciss
        if item[2] == "X":  
            score += 2
        elif item[2] == "Y":
            score += 6
        else:
            score += 7

print(score)