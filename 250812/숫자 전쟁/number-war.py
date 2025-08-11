n = int(input())
first_cards = [0] + list(map(int, input().split()))
second_cards = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1) : 
    for j in range(1, n + 1) : 
        if second_cards[i] < first_cards[j] : 
            dp[i][j] = dp[i - 1][j] + second_cards[i]

result = 0
for i in range(n + 1) : 
    result = max(result, max(dp[i]))
print(result)