str = input().upper()
dic = [0] * 27
for i in range(0,26):
    dic[i] = str.count(chr(i+65))

most_count = max(dic)

if dic.count(most_count) > 1:
    print("?")
else:
    print(chr(dic.index(most_count)+65))
