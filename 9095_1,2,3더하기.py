r = int(input())
for i in range(r):
    count = 0 
    def jaegui(left):
        if left == 0:
            global count 
            count += 1
            return 
        for i in range(1,4):
            if left - i >= 0:
                jaegui(left-i)
            elif left - i < 0:
                continue
                
                
    n = int(input())
    jaegui(n)
    print(count) 