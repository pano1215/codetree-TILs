n = int(input())
memo = [-1 for _ in range(n*2)]

def fifo(n) :
    if memo[n] != -1 :
        return memo[n]
    elif n <= 2 :
        memo[n] = 1
    else :
        memo[n] = fifo(n - 1) + fifo(n - 2)
    return memo[n]

fifo(n)
print(memo[n])