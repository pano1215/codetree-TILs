n, m = map(int, input().split()) # 보석 수, 무게 
w, v = zip(*[tuple(map(int, input().split())) for _ in range(n)])
w, v = list(w), list(v)

dp = [0 for _ in range(m + 1)]

for i in range(n) : # 가방
    for j in range(1, m + 1) : # 무게
        if j - w[i] >= 0 :
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    #print(dp)
        

print(max(dp))