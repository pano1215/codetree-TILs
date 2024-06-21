from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

q = deque()

def is_range(x, y) :
    return 0 <= x < n and 0 <= y < m

# 이동가능한 경우란 : visited False, 뱀이 없는 곳(1인 지역)
def can_go(x, y) :
    if not is_range(x, y) :
        return False
    if miro[x][y] == 0 or visited[x][y] :
        return False
    return True

# x y를 반복하며 제시하기 (아래, 위, 오른쪽으로만 이동가능)
def bfs() :
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while q : # q에 값이 있는 경우 계속 반복함
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys) :
            next_x, next_y = x + dx, y + dy
            
            if can_go(next_x, next_y) :
                visited[next_x][next_y] = True

                # q에 이동하는 위치넣기
                q.append([next_x, next_y])

            if next_x == n - 1 and next_y == m - 1 :
                check = 1
                return check
            else : 
                check = 0 
    return check

# bfs 시작
q.append((0,0))
visited[0][0] = True
result = bfs()
print(result)