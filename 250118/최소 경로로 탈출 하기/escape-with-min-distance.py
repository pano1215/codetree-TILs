from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

q = deque()

visited = [[False for _ in range(n)] for _ in range(m)] 
step = [[0 for _ in range(n)] for _ in range(n)]

ans = 0


def in_range(nx, ny) : 
    return 0 <= nx < n and 0 <= ny < n 

def bfs() :
    global ans 

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    while q : 
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) : 
            nx, ny = x + dx, y + dy 

            if in_range(nx, ny) and not visited[nx][ny] and a[nx][ny] == 1 : 
                push(nx, ny, step[x][y] + 1)
                ans += 1 

def push(x, y, s) : 
    step[x][y] = s
    visited[x][y] = True
    q.append((x, y))

push(0, 0, 0)
bfs()

if step[-1][-1] : 
    print(0)
else : 
    print(step[-1][-1])