n = int(input())
dp = [0] * 10000000

def test(n) : 
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5

    if n < 2 :
        return dp[n]
    else :
        for i in range(n) : 
            dp[n] += test(i) * test(n - i - 1)
    return dp[n]
test(n - 1)
print(dp[n])