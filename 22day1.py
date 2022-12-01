f = open('1.txt', 'r')
lines = f.readlines()
temp = []
calories = []

for line in lines:
    line = line[:-1]
    if line != "":
        temp.append(int(line))
    else:
        calories.append(sum(temp))
        temp = []

calories.sort()
print(calories[-1] + calories[-2] + calories[-3])
