A, B = map(int,input().split())
d = set()
b = set()
for i in range(A):
    d.add(input())
for j in range(B):
    b.add(input())

result = sorted(list(d&b))
print(len(result))
for i in result:
    print(i)

# A, B = map(int,input().split())
# d = []
# b = []
# for i in range(A):
#     d.append(input())
# for j in range(B):
#     b.append(input())

# sorted(d)
# sorted(b)

# db = [] 
# for i in d:
#     if i in b:
#         db.append(i)
# print(len(db))
# for i in range(len(db)):
#     print(db[i])

# A, B = map(int,input().split())
# lst = []
# res = []
# for i in range(A+B):
#     lst.append(input())
# for j in range(len(lst)):
#     if lst.count(lst[j]) == 2:
#         res.append(lst[j])
#         result = set(res)
# print(len(result))
# for i in result:
#     print(i)