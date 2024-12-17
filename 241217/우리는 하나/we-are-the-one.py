from itertools import combinations
from collections import deque
import sys

n, k, u, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def height(x, y, nx, ny) :
    return u <= abs(arr[x][y] - arr[nx][ny]) <= d

def can_go(nx, ny) :
    return 0 <= nx < n and 0 <= ny < n 

def bfs(com) :
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque(com)

    #print(com, visited, q)

    for x, y in com :
        visited[x][y] = True
        cnt += 1

    while q : 
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) : 
            nx, ny = x + dx, y + dy

            if can_go(nx, ny) and height(x, y, nx, ny) and not visited[nx][ny] : 
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))

    return cnt

# 도시 좌표 만들기
cities = [(i, j) for i in range(n) for j in range(n)]
max_cnt = -sys.maxsize
for com in combinations(cities, k) : 
    max_cnt = max(max_cnt, bfs(com))
print(max_cnt)