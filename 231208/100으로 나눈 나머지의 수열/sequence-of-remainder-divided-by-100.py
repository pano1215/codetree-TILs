n = int(input())
first = 2
second = 4

def re(n) :
    if n == 1 :
        return 2
    if n == 2 :
        return 4
    
    return (re(n - 1) * re(n - 2)) % 100

print(re(n))