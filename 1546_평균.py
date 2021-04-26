n = int(input())
a = [int(input()) for _ in range(n)]
lst = []
for i in range(n):
    lst.append(a[i]/max(a)*100)

print(sum(lst)/len(lst))
# 웁스
