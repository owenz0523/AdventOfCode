f = open('2.txt', 'r')
lines = f.readlines()
scoring = {"R": 1, "P": 2, "S": 3}
guideWin = {"A": "P", "B": "S", "C": "R"}
guideDraw = {"A": "R", "B": "P", "C": "S"}
guideLose = {"A": "S", "B": "R", "C": "P"}
score = 0

for line in lines:
    n1 = line[0]
    result = line[2]
    if result == "X":
        n2 = guideLose[n1]
        score += scoring[n2] + 0
    elif result == "Y":
        n2 = guideDraw[n1]
        score += scoring[n2] + 3
    else:
        n2 = guideWin[n1]
        score += scoring[n2] + 6

print(score)