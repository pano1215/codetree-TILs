n = int(input())
memo = [-1] * (n * 2)

def test(n) :
    memo[0] = 1
    memo[1] = 1
    memo[2] = 7
    memo[3] = 22
    memo[4] = 71

    if memo[n] != -1 :
        return memo[n]
    
    if n >= 5 :
        memo[n] = (test(n - 1) * 3) + test(n - 2) - test(n - 3)
    
    return memo[n]
test(n)
print(memo[n] % 1000000007)