n = int(input())

memo = [-1] * 10007

def test(n) :
    if memo[n] != -1 :
        return memo[n]

    if n <= 2 :
        memo[n] = n
    else :
        memo[n] = test(n - 1) + test(n - 2)
    return memo[n]

test(n)
print(memo[n] % 10007)