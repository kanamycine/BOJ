n, c = map(int, input().split())
arr = list(map(int, input().split()))
lst = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i] + arr[j] + arr[k] <= c:
                lst.append(arr[i] + arr[j] + arr[k])

print(max(lst))
