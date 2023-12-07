n = int(input())

def odds(n) :
    if n == 1 :
        return n
    return n + odds(n - 2)

def even(n) :
    if n == 2 :
        return n
    return n + even(n - 2)

if n % 2 == 1 :
    print(odds(n))
else :
    print(even(n))