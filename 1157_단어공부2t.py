s = input()
s = s.upper()
lst = [0] * 26
for i in s:
    lst[ord(i) - 65] += 1
a = max(lst)

if lst.count(a) > 1 :
    print("?")
else:
    print(chr(lst.index(a)+65))



