with open("Day4\Day4input") as f:
    data = f.read()
    data = data.splitlines()
sum = 0

for string in data:
    list_ = string.split(",")
    int1 = list_[0].split("-")
    int2 = list_[1].split("-")

# for string in data:
#     i2 = string.rfind("-", 0, 3)+1
#     i4 = string.rfind("-")+1
#     i3 = string.rfind(",") +1

#     string = string.replace("-", " ")
#     string = string.replace(",", " ")

#     val1 = int(string[:2])
#     val2 = int(string[i2:i2+2])
#     val3 = int(string[i3:i3+2])
#     val4 = int(string[i4:i4+2])

#     if ((val1 >= val3) and (val1 <= val4)) or \
#         ((val2 >= val3) and (val2 <= val4)) or \
#         ((val3 >= val1) and (val3 <= val2)) or \
#         ((val4 >= val1) and (val4 <= val2)):
#         sum += 1

print(sum)


    