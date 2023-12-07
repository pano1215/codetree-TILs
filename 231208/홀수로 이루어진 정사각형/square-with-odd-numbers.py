n = int(input())

num = 11
for i in range(n) :
    #num = 11
    for j in range(n) :
        print(i * 2 + j * 2 + 11, end = ' ')
        num += 2
    print()