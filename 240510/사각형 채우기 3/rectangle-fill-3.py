n = int(input())
memo = [-1] * 1000

def test(n) :
    memo[0] = 1
    memo[1] = 2
    memo[2] = 7

    if memo[n] != -1 :
        return memo[n]
    
    if n >= 3 :
        memo[n] = (test(n - 1) * 3) + test(n - 2) - test(n - 3)
    
    return memo[n]
test(n)
print(memo[n] % 1000000007)