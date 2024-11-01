n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
temp_arr = [[0 for _ in range(n)] for _ in range(n)]

temp_arr[0][0] = arr[0][0]
for i in range(1, n) :
    temp_arr[i][0] = max(temp_arr[i - 1][0], arr[i][0])
    temp_arr[0][i] = max(temp_arr[0][i - 1], arr[0][i])

for row in range(1, n) :
    for col in range(1, n) :
        temp_arr[row][col] = min(max(temp_arr[row - 1][col], arr[row][col]), max(temp_arr[row][col - 1], arr[row][col]))
        
print(temp_arr[-1][-1])