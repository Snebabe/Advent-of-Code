with open("Day1\day1input.txt") as file:
    input = file.read()
    input = input.splitlines()

calories = []
total = []

for value in input:
    if value != "":
        calories.append(int(value))
    else:
        total.append(sum(calories))
        calories = []
        
total.sort()
print(total[-1]+ total[-2]+ total[-3])
