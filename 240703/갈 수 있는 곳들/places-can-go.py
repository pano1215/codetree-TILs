from collections import deque

# 입력값 받기
n, k = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
point = [list(map(int, input().split())) for _ in range(k)]
cnt = 0

# 방문 배열 생성
visited = [[False for _ in range(n)] for _ in range(n)]

# deque 생성
q = deque()

# 갈 수 있는 범위인지 판단하기
def is_range(next_x, next_y) : 
    return 0 <= next_x < n and 0 <= next_y < n

# 갈 수 있는지 판단하기
def can_go(next_x, next_y) :
    if not is_range(next_x, next_y) :
        return False
    if miro[next_x][next_y] == 1 or visited[next_x][next_y] :
        return False
    
    return True

# x y를 반복하며 제시하기 (아래, 위, 오른쪽으로만 이동가능)
def bfs() :
    global cnt 

    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    
    while q : # q에 값이 있는 경우 계속 반복함 
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys) : 
            next_x, next_y = x + dx, y + dy

            if can_go(next_x, next_y) : 
                visited[next_x][next_y] = True
                q.append((next_x, next_y))
                cnt += 1
                #print(next_x, next_y)
    return cnt

# bfs 시작
for spot in point :
    cnt  += 1
    r, c =spot[0] - 1, spot[1] - 1
    q.append((r, c))
    visited[r][c] = True
    result = bfs()
    #print(visited)
    # 방문 배열 원복
    visited = [[False for _ in range(n)] for _ in range(n)]

print(result)