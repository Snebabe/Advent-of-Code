with open("Day6\Day6Input.txt") as f:
    data = f.read()
    data = data.splitlines()

tmp_string = ""

for value in data:
    for index, char in enumerate(value):
        if index < 14:
            tmp_string += char
        else:
            count = 0
            for i, compare in enumerate(tmp_string):
                if compare in tmp_string[:i]:
                    count += 1
            if count == 0:
                print(index)
                break
            tmp_string += char
            tmp_string = tmp_string[1:]

