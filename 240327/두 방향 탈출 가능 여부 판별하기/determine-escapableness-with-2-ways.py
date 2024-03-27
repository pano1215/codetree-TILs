n, m = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

# 격자 안에서 벗어나는지 아닌지 체크하는 함수
def is_in_range(next_x, next_y) :
    return 0 <= next_x < n and 0 <= next_y < m

# 탈출가능한지 확인하기 
def escape(next_x, next_y) :
    global escape_yes_or_no

    if next_x == n - 1 and next_y == m - 1 :
        escape_yes_or_no = 1 # 탈출가능
    
    # if escape_yes_or_no == 1 or escape_yes_or_no == 0 :
    #     print(escape_yes_or_no)
    # return

# 이동이 가능한지 확인하는 함수
def can_go(next_x, next_y) :
    # 이동가능하다는 것
    # 1. 격자 안에서 벗어나지 말아야 함
    if not is_in_range(next_x, next_y) :
        # 격자에서 벗어난다면 이동못함 
        return False

    # 2. [next_x][next_y]가 0이나 2가 아니고,
    # 3. visted[next_x][next_y]가 True가 아닌 경우
    if arr[next_x][next_y] != 1 or visited[next_x][next_y] :
        return False
    return True

def dfs(x, y) :
    dxs = [0, 1]
    dys = [1, 0]

    for dx, dy in zip(dxs, dys) :
        # next_x, next_y 세팅
        next_x = x + dx
        next_y = y + dy

        # 이동이 가능한지 확인
        if can_go(next_x, next_y) :
             
            arr[next_x][next_y] = 2 # 이동가능하다면 [next_row][next_col]를 2로 세팅
            visited[next_x][next_y] = True # 방문한거 체크 
            dfs(next_x, next_y) # dfs 재호출

            # 탈출가능한지 확인하기 
            escape(next_x, next_y)

def Print():
    print(escape_yes_or_no)

# 세팅
escape_yes_or_no = 0 # 탈출가능여부
arr[0][0] = 2 # [0][0]에서 시작하는거 세팅하기
visited[0][0] = True # visited [0][0] 방문체크
dfs(0, 0)
Print()