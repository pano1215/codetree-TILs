# deque import
from collections import deque

# 존재하지 않는 위치 선언(튜플로)
not_exists = (-1, -1)

# n, k(튜플로), grid 입력
n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

# 현재 위치(r, c 입력, 튜플로)
r, c = tuple(map(int, input().split()))

# 현재위치에서 -1하기(인덱스에 맞게, 튜플로)
curr_cell = (r - 1, c - 1)

# deque 선언
bfs_q = deque()

# visited 배열 선언
visited = [[0 for _ in range(n)] for _ in range(n)]

# in_range : 격자 범위 내에 있는지 체크
def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

# can_go 이동할 수 있는 경우 : 격자 범위 안에 있는 경우, 방문한 적이 없는 경우, 현재 숫자보다 작은 경우
def can_go(x, y, target_num) :
    return in_range(x, y) and not visited[x][y] and grid[x][y] < target_num

# initialize_visited : visited 배열을 초기화 해줍니다.
def initialize_visited() :
    for i in range(n) :
        for j in range(n) :
            visited[i][j] = False

# Step1. BFS를 진행하여 갈 수 있는 모든 위치를 탐색합니다.
def bfs() : 
    
    # dxs, dys : 이동가능한 좌표 설정
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # 현재 위치 선언 : 튜플 해제 
    curr_x, curr_y = curr_cell

    # visited 방문한 위치 체크
    visited[curr_x][curr_y] = True

    # bfs_q 큐에 현재 위치 담기
    bfs_q.append(curr_cell)

    # target_num : 현재 위치의 숫자 
    target_num = grid[curr_x][curr_y]

    # BFS 탐색을 수행합니다.
    # 큐에 값이 없을 때까지 반복 
    while bfs_q :
        # bfs_q 큐에서 맨 앞에 있는 값(왼쪽)부터 차례로 빼기   
        curr_x, curr_y = bfs_q.popleft()

        # dxs, dys 반복하며 이동할 위치 설정 
        for dx, dy in zip(dxs, dys) :
            # new_x, new_y 연산 
            new_x, new_y = curr_x + dx, curr_y + dy

            # can_go : 이동 가능한지 체크
            if can_go(new_x, new_y, target_num) :
                # 이동 가능하다면
                # bfs_q에 이동가능한 새로운 좌표(튜플) 넣기
                bfs_q.append((new_x, new_y))

                # visited 새로 방문한 위치 체크 
                visited[new_x][new_y] = True

# need_update : best 위치를 새로운 위치로 바꿔줘야 하는지를 판단합니다.
def need_update(best_pos, new_pos) :
    # 첫 도달 가능한 위치라면
    # update가 필요합니다.
    if best_pos == not_exists :
        return True

    # best_pos, new_pos의 x y 좌표 선언
    best_x, best_y = best_pos
    new_x, new_y = new_pos

    # 숫자, -행, -열 순으로 더 큰 곳이 골라져야 합니다.
    return (grid[new_x][new_y], -new_x, -new_y) > (grid[best_x][best_y], -best_x, -best_y)

# move : 가장 우선순위가 높은 위치를 찾아 위치를 이동합니다.
def move() :
    # 현재 위치 global 선언
    global curr_cell 

    # initialize_visited() : BFS 탐색을 위한 초기화 작업을 수행합니다.
    initialize_visited()

    # Step1. BFS를 진행하여 갈 수 있는 모든 위치를 탐색합니다.
    bfs()

    # Step2. 
    # best_pos : 도달 할 수 있는 위치들 중 가장 우선순위가 높은 위치를 구합니다.
    best_pos = not_exists

    # 격자 전체를 반복하며 도달 불가능한 곳, 업데이트가 필요한 곳 체크
    for i in range(n) :
        for j in range(n) :
            # 도달이 불가능하거나 현재 위치는 건너뜁니다.
            if not visited[i][j] or (i, j) == curr_cell :
                continue

            # new_pos : 새로운 위치(튜플) 선언
            new_pos = (i, j)

            # need_update 새로운 위치로 바꿔줘야 하는지 판단 
            if need_update(best_pos, new_pos) :
            # 새로운 위치로 바꿔야 한다면
                # 우선순위 위치를 새로운 위치로 변경
                best_pos = new_pos

    # Step3. 위치를 이동합니다.
    # 만약 움직일 위치가 없다면 종료합니다.
    if best_pos == not_exists :
        return False
    # 움직일 위치가 있다면 이동합니다. 
    else :
        curr_cell = best_pos
        return True 

# k번에 걸쳐 움직이는 것을 반복합니다.
for _ in range(k) : 
    # 움직여야 하는지 판단
    is_move = move()

    # 움직이지 못했다면 바로 종료합니다.
    if not is_move :
        break

# 현재 위치가 최종 x y 
final_x, final_y = curr_cell

# 결과 출력
print(final_x + 1, final_y + 1)