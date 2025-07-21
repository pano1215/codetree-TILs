import sys

n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

MAX_EXP = 100_001  # 충분히 큰 경험치 총합 상한

# dp[exp] = exp 경험치를 얻기 위한 최소 시간
dp = [sys.maxsize] * MAX_EXP
dp[0] = 0  # 경험치 0일 때 시간 0

for exp, time in quests:
    for i in range(MAX_EXP - 1, exp - 1, -1):
        if dp[i - exp] != sys.maxsize:
            dp[i] = min(dp[i], dp[i - exp] + time)

# 이제 m 이상인 경험치 중 가장 작은 dp[i]를 찾는다
answer = sys.maxsize
for i in range(m, MAX_EXP):
    if dp[i] < answer:
        answer = dp[i]

print(answer if answer != sys.maxsize else -1)
