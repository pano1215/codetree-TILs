from itertools import combinations
from collections import deque

def height(h1, h2) :
    return u <= abs(h1 - h2) <= d

def can_go(nx, ny) :
    global visited
    return 0 <= nx < n and 0 <= ny < n 

def bfs(select_city) : 
    cnt = 0 
    q = deque(select_city)
    visited = [[False for _ in range(n)] for _ in range(n)]

    for x, y in select_city :
        visited[x][y] = True
        cnt += 1

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q : 
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy 

            if can_go(nx, ny) and height(arr[x][y], arr[nx][ny]) and not visited[nx][ny] :
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))
    return cnt 

# 입력받기 
n, k, u, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 최대 도시 선언하기 
max_cities = 0 

# 모든 도시 조합 만들기
cities = [(i, j) for i in range(n) for j in range(n)]
for select_city in combinations(cities, k) :
    max_cities = max(max_cities, bfs(select_city))

print(max_cities)