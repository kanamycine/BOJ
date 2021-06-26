sum = 0

for i in range(1, 10):
    for j in range(10):
        if j % 3 == 0 :
            continue
        if i % 4 == 0:
            break
            sum += 1
print(sum)