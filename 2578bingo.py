arr = [list(map(int,input().split()))for _ in range(5)]
print(arr)

answer = [list(map(int,input().split()))for _ in range(5)]

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if arr[i][j] == answer[k][l]:
                    arr[i][j] == 0