with open("Day5\Day5Input.txt") as f:
    data = f.read()
    data = data.splitlines()

stack = [[], [], [], [], [], [], [], [], []] 

for index, value in enumerate(data):
    stackindex = 0
    if index < 8:
        while value:
            if value[:4] != "    ":
                stack[stackindex].insert(0, value[1])
            value = value[4:]
            print(stack)
            stackindex += 1
    if index > 9:
        nums = value.split()
        tmp_list = []
        for _ in range(int(nums[1])):
            tmp_list.append(stack[int(nums[3])-1][len(stack[int(nums[3])-1])-1])
            stack[int(nums[3])-1].pop()
        tmp_list.reverse()
        for item in tmp_list:
            stack[int(nums[5])-1].append(item)
        
print("done")