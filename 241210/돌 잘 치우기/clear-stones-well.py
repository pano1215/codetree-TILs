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

# 가장 큰 방문 수 구하는 함수 
def find_max(cnt) :
    global max_num
    max_num = max(max_num, cnt)

def is_range(x, y) :
    return 0 <= x < n and 0 <= y < n
    
# 이동가능한 경우란 : visited False, 돌이 없는 곳(0인 지역)
def can_go(x, y) :
    global temp_miro, visited, cnt

    if not is_range(x, y) :
        return False
    if temp_miro[x][y] == 1 or visited[x][y] :
        return False
    return True

# 호출 : BFS 
def bfs() : 
    global temp_miro, visited, cnt

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q : # q에 값이 있는 경우 계속 반복함
        x, y = q.popleft()
        #print('x, y : ', x, y)
        for dx, dy in zip(dxs, dys) :
            next_x, next_y = x + dx, y + dy

            if can_go(next_x, next_y) :
                visited[next_x][next_y] = True
                cnt += 1
                # q에 이동하는 위치넣기
                q.append((next_x, next_y))

            #print('visited : ', visited, cnt)
    
    # 호출 : 가장 큰 방문 수 구하는 함수 
    find_max(cnt)

# 만들어진 조합(stone_com)의 돌을 치우기 
def delete_stone(stone_com) :
    global temp_miro, visited, cnt

    # temp_miro 초기화하기 
    temp_miro = [row[:] for row in miro]

    # cnt 초기화하기
    cnt = 0

    # visited 초기화하기
    #visited = [[False for _ in range(n)] for _ in range(n)]

    for row, col in stone_com :
        temp_miro[row][col] = 0
    
    #if stone_com[0] == (2, 3) and stone_com[1] == (3, 1) :
    #print('temp_miro : ', temp_miro)

    # 돌아가며 시작점마다 bfs 돌리기 
    for row, col in start_points : 
        #print('start_points : ', start_points, row, col)
        q.append((row, col))

        if not visited[row][col] : 
            visited[row][col] = True
            cnt += 1
        # 호출 : bfs
        bfs()

    # visited 초기화하기
    visited = [[False for _ in range(n)] for _ in range(n)]

# 치우는 돌의 조합 만드는 함수
stone_com = []
def make_com(num) :
    global temp_miro, visited, cnt

    if len(stone_com) == m :
        #print('stone_com : ', stone_com)

        # 호출 : 만들어진 조합(stone_com)의 돌을 치우기 
        delete_stone(stone_com)
        return 

    for i in range(num, len(stone_points)) :
        stone_com.append((stone_points[i]))
        make_com(i + 1)
        stone_com.pop()

# 호출 : 치우는 돌의 조합 만드는 함수
make_com(0)

print(max_num)