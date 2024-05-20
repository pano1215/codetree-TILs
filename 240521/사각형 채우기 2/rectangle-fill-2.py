n = int(input())
memo = [0] * 10000000

def test(n) :
    if memo[n] != 0 :
        return memo[n]
    
    if n <= 1 :
        return 1
    
    if n % 2 == 0 : # n이 짝수인 경우
        memo[n] = (test(n - 1) * 2) + 1
    else :
        memo[n] = (test(n - 1) * 2) - 1
    return memo[n]

result = test(n)
print(result % 10007)