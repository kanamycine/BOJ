import sys
lst = [int(input()) for _ in range(9)]
total = sum(lst)
lst.sort()
n = 9

for i in range(0,n):
    for j in range(i+1, n):
        if total - lst[i] - lst[j] == 100:
            for k in range(0, n):
                if i==k or j==k:
                    continue
                print(lst[k]) # i와 k는 건너뛰고 출력해야지 ? gg
            sys.exit(0)#