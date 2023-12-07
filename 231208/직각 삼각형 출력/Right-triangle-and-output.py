n = int(input())
i = 1
for _ in range(1, n+1) :
    for j in range(i) :
        print("*", end='')
    i += 2
    print()
        
    #for j in range(i) :
    #print('*' * i)