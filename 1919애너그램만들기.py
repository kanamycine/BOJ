# s1 = list(input())
# s2 = list(input())

# for i in s1:
#     if i not in s2:
#         s1.remove(i)

# for j in s2:
#     if j not in s1:
#         s2.remove(i)

# print(s1, s2)

s1 = ['a','a','b','b','c','c']
s2 = ['x','x','y','y','b','b']
r1 = s1
for i in s1:
    if i not in s2:
        r1.remove(i)
s1.remove('a')
print(r1)