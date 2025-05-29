n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
jobs.sort()

dp = [0] * n

for i in range(n) :
    dp[i] = jobs[i][2]

    for j in range(i) : 
        i_str_day = jobs[i][0]
        j_end_day = jobs[j][1]

        #print(i_str_day, j_end_day)
        if j_end_day < i_str_day :
            dp[i] = max(dp[i], jobs[i][2] + jobs[j][2])
            #print(dp)

print(max(dp))