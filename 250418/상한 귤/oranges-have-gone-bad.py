from collections import deque 

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
step_arr = [[0 for _ in range(n)] for _ in range(n)]

def is_range(x, y) : 
    return 0 <= x < n and 0 <= y < n 

def can_go(x, y) :
    return is_range(x, y) and not visited[x][y] and arr[x][y] == 1

def push(x, y, step_cnt) : 
    q.append((x, y))
    step_arr[x][y] = step_cnt
    visited[x][y] = True

def dfs() : 
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q : 
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny) :
                push(nx, ny, step_arr[x][y] + 1)

for row in range(n) : 
    for col in range(n) : 
        if arr[row][col] == 2 :
            push(row, col, 0)
dfs()

for row in range(n) : 
    for col in range(n) : 
        if arr[row][col] == 0 :
            step_arr[row][col] = -1 
        elif arr[row][col] == 1 and step_arr[row][col] == 0 :
            step_arr[row][col] = -2

for row in step_arr :
    for num in row :
        print(num, end = ' ')
    print()