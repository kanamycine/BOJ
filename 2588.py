fst = int(input())
sec = int(input())

print(fst * (sec % 10))
print(fst * ((sec % 100) // 10))
print(fst * (sec // 100))
print(fst * sec)
