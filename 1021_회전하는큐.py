A, B = map(int, input().split()) # 10 3
lst = list(map(int, input().split()))  # 1 2 3
res = 0
cq = [i for i in range(1, A+1)] # [1,2,3,4,...10]
cnt = 0

for i in range(B):
    while True :
        if lst[i] == cq[0]:
            del cq[0]
            res += cnt
            cnt = 0
            break
        else:
            if cq.index(lst[i]) - len(cq)//2 <= 0:
                cq.append(cq[0])
                del cq[0]
                cnt += 1#
            else:
                cq.insert(0, cq[-1])
                del cq[-1] 
                cnt += 1
print(res)