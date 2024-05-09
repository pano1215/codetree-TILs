n = int(input())
memo = [-1] * 10007

def test(n):
    if memo[n] != -1 :
        return memo[n] 
    elif n <= 4:
        memo[n] = 1
    else :
        memo[n] = test(n - 2) + test(n - 3)
    
    return memo[n]

test(n)
print(memo[n]  % 10007)