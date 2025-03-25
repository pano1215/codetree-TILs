import sys
from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
steps = [[0 for _ in range(n)] for _ in range(n)]
ans = sys.maxsize
inf = sys.maxsize

def is_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def can_go(x, y) : 
    return is_range(x, y) and not visited[x][y]

def push(x, y, step) :
    q.append((x, y))
    visited[x][y] = True
    steps[x][y] = step

def dfs() : 
    global ans 

    dxs = [-2, -2, -1, -1,  1, 1,  2, 2] 
    dys = [-1,  1, -2,  2, -2, 2, -1, 1] 

    while q : 
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y) :
                push(new_x, new_y, steps[x][y] + 1) 

    if visited[r2][c2] : 
        ans = steps[r2][c2]

push(r1, c1, 0)
dfs()

if ans == inf : 
    print(-1)
else :
    print(ans)