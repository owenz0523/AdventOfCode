lines = 2251
temp = []
calories = []

for i in range(lines):
    n = input()
    if n != "":
        temp.append(int(n))
    else:
        calories.append(sum(temp))
        print(calories)
        temp = []

calories.sort()
print(calories[-1] + calories[-2] + calories[-3])