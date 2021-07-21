n = int(input())
lst = list(map(int,input().split()))
x = int(input())
count = 0
while(len(lst)!=0):
    if x - lst[0] in lst and x - lst[0] != lst[0] : 
        count+=1
        del lst[0]
    else:
        del lst[0]
print(count)