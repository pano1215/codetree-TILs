n, m = map(int, input().split()) # 보석 수, 무게 
w, v = zip(*[tuple(map(int, input().split())) for _ in range(n)])
w, v = list(w), list(v)

# print(n, m, w, v)

dp = [0 for _ in range(m + 1)]
dp[0] = 0

for i in range(n) : # 가방
    for j in range(m, w[i] -1, -1) : # 무게
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(max(dp))