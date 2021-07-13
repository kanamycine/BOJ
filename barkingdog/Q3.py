n = int(input())
result = 0
for i in range(1, n):
    if i * i == n:
        result = 1
        break
    elif i * i > n :
        break
print(result)
