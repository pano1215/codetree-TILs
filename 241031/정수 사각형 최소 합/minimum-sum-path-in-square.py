n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sum_arr = [[0 for _ in range(n)] for _ in range(n)]

# 가로 세로 채우기 
sum_arr[0][-1] = arr[0][-1]
for i in range(1, n) :
    sum_arr[0][n - i - 1] = sum_arr[0][n - i] + arr[0][n - i - 1]
    sum_arr[i][n - 1] = sum_arr[i - 1][n - 1] + arr[i][n - 1]

# 나머지 칸 채우기 
for row in range(1, n) :
    for col in range(n - 2, -1, -1) :
        sum_arr[row][col] = min(arr[row][col] + sum_arr[row - 1][col], arr[row][col] + sum_arr[row][col + 1])

print(min(sum_arr[-1]))