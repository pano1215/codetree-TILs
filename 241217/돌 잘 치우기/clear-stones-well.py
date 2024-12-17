from collections import deque

n, k, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
start_points = [tuple(x - 1 for x in map(int, input().split())) for _ in range(k)]

temp_miro = [row[:] for row in miro]
visited = [[False for _ in range(n)] for _ in range(n)]

cnt = 0
max_num = -1

q = deque()

stone_points = []
for row in range(n) :
    for col in range(n) :
        if miro[row][col] == 1 :
            stone_points.append((row, col))

def find_max(cnt) : 
    global temp_miro, visited, max_num

    max_num = max(max_num, cnt)

def bfs() : 
    global temp_miro, visited, cnt

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q : 
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) :
            nx, ny = x + dx, y + dy 

            if 0 <= nx < n and 0 <= ny < n and not temp_miro[nx][ny] == 1 and not visited[nx][ny] :
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))

    find_max(cnt)

def delete_stone(stone_com) : 
    global temp_miro, visited, cnt

    temp_miro = [row[:] for row in miro]

    cnt = 0

    for row, col in stone_com : 
        temp_miro[row][col] = 0 

    for row, col in start_points :
        q.append((row, col))

        if not visited[row][col] : 
            visited[row][col] = True
            cnt += 1
        bfs()

    visited = [[False for _ in range(n)] for _ in range(n)]

stone_com = []
def make_com(num) :
    global temp_miro, visited, cnt

    if len(stone_com) == m : 
        #print('stone_com : ', stone_com)
        delete_stone(stone_com)
        return

    for i in range(num, len(stone_points)) :
        stone_com.append((stone_points[i]))
        make_com(i + 1)
        stone_com.pop()

make_com(0)

print(max_num)