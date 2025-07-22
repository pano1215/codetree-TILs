import sys

n, m = map(int, input().split()) # n : 퀘스트 정보, m : 총 합 
quests = [tuple(map(int, input().split())) for _ in range(n)]

# dp[i] = i시간 동안 얻을 수 있는 최대 경험치
dp = [-1] * (m + 1)
dp[0] = 0

for exp, time in quests :  # 순서 주의! (exp, time)
    for i in range(m, time - 1, -1) :
        if dp[i - time] != -1 : 
            dp[i] = max(dp[i], dp[i - time] + exp)

            #print(dp)
min_val = -sys.maxsize 
for i in range(1, len(dp)) : 
    if dp[i - 1] < dp[i] : 
        min_val = max(i, min_val)
    
        if dp[min_val] >= m : 
            break 
#print(dp, min_val, dp[min_val])
if dp[min_val] >= m : 
    print(min_val)
else : 
    print(-1)
