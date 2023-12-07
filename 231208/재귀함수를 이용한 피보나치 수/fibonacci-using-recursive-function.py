n = int(input())

def f(n) :
    # one, two = 1, 1

    # for _ in range(n) : 
    #     one, two = two, one + two
    # return two - one
    if n <= 2 :
        return 1

    return f(n - 1) + f(n - 2) 

print(f(n))