s = input()
total = 0
for i in s:
    count = 3
    x = ord(i)-65
    count += x // 3
    total += count
print(total)
