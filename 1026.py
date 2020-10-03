N = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

check1 = []
check2 = []

for i in lst1:
    check1.append(i)
for i in lst2:
    check2.append(i)

check1.sort()
check2.sort()

res = 0
for i in range(N):
    res += check1[i] * check2[-i-1]
print(res)
##gkrltlfge   bvhvhf