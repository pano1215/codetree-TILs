import sys
sys.setrecursionlimit(250000)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
temp_arr = [[0 for _ in range(n)] for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def is_range(next_row, next_col) :
    return 0 <= next_row < n and 0 <= next_col < n

def dfs(row, col) :
    if temp_arr[row][col] != 0:
        return temp_arr[row][col]

    temp_arr[row][col] = 1  

    for dx, dy in zip(dxs, dys) : 
        next_row, next_col = row + dx, col + dy
        if is_range(next_row, next_col) and arr[row][col] < arr[next_row][next_col] :
            temp_arr[row][col] = max(temp_arr[row][col], dfs(next_row, next_col) + 1)
    
    return temp_arr[row][col]

max_steps = 0
for row in range(n) : 
    for col in range(n) :
        max_steps = max(max_steps, dfs(row, col))

print(max_steps)