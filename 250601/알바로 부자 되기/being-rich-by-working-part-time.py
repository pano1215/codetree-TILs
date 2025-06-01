n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
jobs.sort()

dp = [0] * n 

for i in range(n) :
    dp[i] = jobs[i][2]
    
    for j in range(n) : 
        i_str_time = jobs[i][0]
        j_str_time = jobs[j][1]

        if i_str_time > j_str_time :
            dp[i] = max(dp[i], dp[j] + jobs[j][2])

print(max(dp))

        