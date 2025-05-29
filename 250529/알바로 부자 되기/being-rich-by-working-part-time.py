n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
jobs.sort()

dp = [0] * n

for i in range(n) :
    dp[i] += jobs[i][2]

    for j in range(i) : 
        i_end_day = jobs[i][1]
        j_end_day = jobs[j][1]

        if j_end_day > i_end_day :
            price = max(dp[i], jobs[j][2])

print(max(dp))