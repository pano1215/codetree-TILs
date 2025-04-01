import itertools
from collections import deque
import sys 

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

visited = []
step_arr = []
temp_ans = sys.maxsize # 걸음수 기록 
maxsize = sys.maxsize

def is_range(x, y) : 
    return 0 <= x < n and 0 <= y < n 

def can_go(x, y) :
    return is_range(x, y) and not visited[x][y] and temp_arr[x][y] == 0 

def push(x, y, step) :
    q.append((x, y))
    visited[x][y] = True
    step_arr[x][y] = step

def bfs() : 
    global temp_ans

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q : 
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny) :
                push(nx, ny, step_arr[x][y] + 1)

    if visited[r2][c2] : 
        temp_ans = min(step_arr[r2][c2], temp_ans)
                
# 벽이 있는(1) 좌표 구하기
# k 수에 맞는 좌표 조합구하기 
# 각 조합을 돌아가며 벽을 없앤 배열 생성 > 한 번 턴하면 다시 초기화 
# 벽을 없앤 temp_arr을 반복하며 bfs 
# 도착점까지 도달하는 최소 이동 시간 구하기

# 벽이 있는(1) 좌표 구하기
point_arr = []
for row in range(n) : 
    for col in range(n) : 
        if arr[row][col] == 1 : 
            point_arr.append((row, col))

# k 수에 맞는 좌표 조합구하기 
combinations = itertools.combinations(point_arr, 2)

# 벽을 없앨 임시 배열만들기
temp_arr = []
q = deque()

for points in combinations :
    temp_arr = [row[:] for row in arr]
    visited = [[False for _ in range(n)] for _ in range(n)]
    step_arr = [[0 for _ in range(n)] for _ in range(n)]
    for x, y in points : 
        if temp_arr[x][y] == 1 :
            temp_arr[x][y] = 0 
    
    push(r1, c1, 0)
    bfs()
    q = deque() # 큐 초기화

if sys.maxsize == temp_ans : 
    print(-1)
else : 
    print(temp_ans)