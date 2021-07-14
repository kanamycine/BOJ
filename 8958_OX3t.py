n = int(input())
for i in range(n):
    s = input()
    combo = 0
    score = 0
    for i in s:
        if i == 'O' :
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)