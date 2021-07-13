a = [1,52,48]
n = 3
result = 0
for i in range(len(a)-1):
    for j in range(2, len(a)):
        if a[i] + a[j] == 100:
            result = 1
        break 

print(result)
