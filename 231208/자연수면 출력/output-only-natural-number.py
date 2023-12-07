a, b = map(int, input().split())

if a <= 0 :
    print(0)

if a > 0 :
    for i in range(b) :
        print(a, end = '')