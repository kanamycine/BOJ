arr = [['']* 15 for i in range(5)]
for i in range(5):
    str = list(input())
    str_len = len(str)
    for j in range(str_len):
        arr[i][j] = str[j]

for i in range(15):
    for j in range(5):
        print(arr[j][i], end='')
