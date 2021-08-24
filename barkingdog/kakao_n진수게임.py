n, t, m, p = map(str, input().split())


res = ''
full_res = []
def change(n, b):
    str = "0123456789ABCDEF"
    q, r = divmod(n, b)
    if q == 0:
        return str[r]
    else:
        return change(q,b) + str[r]

for i in range(t*m):
    change_result = change(i,n)
    for k in change_result:
        full_res.append(k)

for i in range(p-1, t*m, m):
    res += full_res[i]

