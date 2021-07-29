n = int(input())
for i in range(n):
    k = int(input())
    n = int(input())
    
    apt = [[ 0 for col in range(n)] for row in range(k+1)]
    for i in range(k+1):
        tmp = 0
        for j in range(n):
            if i == 0:
                apt[i][j] = j + 1
            else:
                tmp += apt[i-1][j]
                apt[i][j] = tmp

    print(apt[i][j])