# from import 정하기 
from itertools import combinations
from collections import deque

# 높이 차가 조건에 맞는지 체크하기
def can_go(h1, h2) :
    global u, d
    return u <= abs(h1 - h2) <= d

# bfs
def bfs(select_city) : 
    count = 0
    q = deque(select_city)
    visited = [[False for _ in range(n)] for _ in range(n)]

    for x, y in select_city :
        visited[x][y] = True 
        count += 1

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q : # q에 값이 있는 경우 계속 반복함
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and can_go(arr[x][y], arr[nx][ny]) :
                count += 1

    return count

# 입력받기 
n, k, u, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 최대 도시 선언하기
max_cities = 0

# 모든 도시의 조합만들기
cities = [(i, j) for i in range(n) for j in range(n)]
for select_city in combinations(cities, k) :
    #print('select_city : ', select_city)
    max_cities = max(max_cities, bfs(select_city))

print(max_cities)
