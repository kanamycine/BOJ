lst = []
for i in range(10000):
    lst.append(i)

arr = []
for i in range(10000):
    sn = 0
    sn += i
    tmp = str(i)
    for j in range(len(tmp)):
        sn += int(tmp[j])
    if sn in lst:
        lst.remove(sn)

for i in lst:
    print(i)