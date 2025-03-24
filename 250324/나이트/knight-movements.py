import sys
from collections import deque

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

ans = sys.maxsize 
inf = sys.maxsize 

# bfs에 필요한 변수
q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

# step[i][j] : 시작점으로부터 (i, j) 지점에 도달하기 위한 
# 최단거리 기록
step = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(new_x, new_y) :
    return 0 <= new_x < n and 0 <= new_y < n

def can_go(new_x, new_y) : 
    return in_range(new_x, new_y) and not visited[new_x][new_y]

# queue에 새로운 위치를 추가하고
# 방문 여부를 표시해줍니다.
# 시작점으로 부터의 최단거리 값도 갱신해줍니다.
def push(x, y, new_step):
    q.append((x, y))
    visited[x][y] = True
    step[x][y] = new_step

def bfs():
    global ans
    
    dxs = [-2, -2, -1, -1,  1, 1,  2, 2] 
    dys = [-1,  1, -2,  2, -2, 2, -1, 1] 
    
    while q : 
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) : 
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y) : 
                push(new_x, new_y, step[x][y] + 1)

    if visited[r2][c2]:
        ans = step[r2][c2]

push(r1, c1, 0)
bfs()

if ans == inf :
    print(-1)
else : 
    print(ans)