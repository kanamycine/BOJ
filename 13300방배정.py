N, K = map(int,input().split())
boy = [0] * 1000
girl = [0] * 1000

for i in range(N):
    S, Y = map(int,input().split())
    if S == 0:
        girl[Y] += 1
    else:
        boy[Y] += 1

for i in range(1,7):
    if (girl[i] % K == 0):
        girl[i] = girl[i] // K
    else:
        girl[i] = girl[i] // K + 1
    
    if (boy[i] % K == 0):
        boy[i] = boy[i] // K
    else:
        boy[i] = boy[i] // K + 1
    
res = sum(girl) + sum(boy)
print(res)