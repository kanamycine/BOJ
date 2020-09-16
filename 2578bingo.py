arr = [list(map(int,input().split()))for _ in range(5)]
check = [0] * 12
cnt = 0

answer = []
for _ in range(5):
    answer += list(map(int,input().split()))

for ans in answer:
    flag = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == ans:
                check[i] += 1
                check[5+j] += 1
                if i == j:
                    check[10] += 1
                if i + j == 4:
                    check[11] += 1
                flag = 1
                cnt += 1
                break
        if flag:
            break
    bingo = 0
    for chk in check:
        if chk == 5:
            bingo +=1
    if bingo >= 3:
        print(cnt)
        break
else:
    print(25)

