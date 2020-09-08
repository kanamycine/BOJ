def prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
                
res = 0
n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    if prime(lst[i]) == True:
        res += 1
print(res)