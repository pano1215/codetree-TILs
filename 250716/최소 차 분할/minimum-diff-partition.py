n = int(input())
arr = list(map(int, input().split()))

total_sum = sum(arr)
max_sum = total_sum // 2

#print(total_sum, max_sum)

dp = [False] * (max_sum + 1)
dp[0] = True

for i in arr : # 제시된 숫자들을 순회함 
    for j in range(max_sum, i - 1, -1) : # dp를 순회함(이때 dp의 idx는 각 집단의 합을 의미함). 중복이 없도록 순회함 
        dp[j] |= dp[j - i]
    #print(dp)

min_val = max_sum
for i in range(max_sum, -1, -1) : 
    if dp[i] : 
        temp_min_val = total_sum - i * 2
        min_val = min(min_val, temp_min_val)
print(min_val)
        #break 