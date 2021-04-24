lst = []
for i in range(10):
    lst.append(int(input()) % 42)
seeet = set(lst)
lst = list(seeet)
print(len(lst))
