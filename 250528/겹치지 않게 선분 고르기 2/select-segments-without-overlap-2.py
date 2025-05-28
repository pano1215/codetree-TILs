n = int(input())
seg = [tuple(map(int, input().split())) for _ in range(n)]
seg.sort()

dp = [0] * n 

for i in range(n) : 
    dp[i] = 1

    for j in range(i) :
        x1, _ = seg[i]
        _, x2 = seg[j]

        if x1 > x2 : 
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))