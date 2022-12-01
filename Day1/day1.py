file = open("day1input.txt", "r")

calories = []
amounts = []

value = file.readline()

for index in range (2246):
    if value == "\n":
        value = file.readline()
        amounts.append(sum(calories))
        calories = []
    else:
        value.replace("\n", "")
        calories.append(int(value))
        value = file.readline()

amounts.sort()
print(amounts[-1]+ amounts[-2]+ amounts[-3])
