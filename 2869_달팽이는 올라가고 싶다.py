A, B, V = map(int, (input().split(" ")))

res = (V-A)/(A-B) + 1
print(int(res))
