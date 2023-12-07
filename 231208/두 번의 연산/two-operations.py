a = int(input())

if a % 2 == 1:
    a = a + 3
    if a % 3 == 0 :
        print(a // 3)
    else : 
        print(a)
else :
    if a % 3 == 0 :
        print(a // 3)
    else : 
        print(a)