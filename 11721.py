string = input()

while len(string) > 10:
    print(string[0:10], end='\n')
    string = string[10:]
if len(string) <= 10:
    print(string)