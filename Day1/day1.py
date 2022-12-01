with open("day1input.txt") as file:
    input = file.read()
    input = input.splitlines()

calories = []
total = []


for value in input:
    if value == "":
        total.append(sum(calories))
        calories = []
    else:
        calories.append(int(value))

total.sort()
print(total[-1]+ total[-2]+ total[-3])
