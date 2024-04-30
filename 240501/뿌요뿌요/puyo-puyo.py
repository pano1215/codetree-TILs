import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)] # 방문 배열 만들기(초기화 상태)
bomb_cnt = 0 # 터지는 블록 변수 선언 
max_cnt = -sys.maxsize # 가장 큰 cnt를 구하기 위한 임시 변수 선언 

# 반환되는 횟수 cnt, 블럭사이즈 구하기 

# 격자 안에서 벗어나는지 아닌지 체크하는 함수
def is_in_range(next_x, next_y) :
    return 0 <= next_x < n and 0 <= next_y < n

# dfs를 반복하면서 0인 곳은 방문 불가로 처리함
def dfs(x, y) :
    global cnt # 블록갯수 전역변수 선언 
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]


    # 이미 방문한 곳은 visted에서 True로 처리해서 방문하지 못하도록 함
    visited[x][y] = True
    arr[x][y] = 0
    cnt += 1 # 블록갯수 cnt

    #print(temp_num, arr)
        
    # 네 방향 중에 전진 가능한 곳을 재호출 
    for dx, dy in zip(dxs, dys) :
        # next_x, next_y 세팅
        next_x = x + dx
        next_y = y + dy

        if is_in_range(next_x, next_y) and temp_num == arr[next_x][next_y] and (arr[next_x][next_y] != 0 or visited[next_x][next_y] == False) :
            dfs(next_x, next_y)

# 모든 배열을 순환하며 dfs(row, col) 호출 - for 
for row in range(n) :
    for col in range(n) : 
        cnt = 0
        if arr[row][col] != 0 and visited[row][col] == False:
            temp_num = arr[row][col] # 숫자가 같은 폭탄만 터트려주기 위함 
            dfs(row, col)
            
            if cnt >= 4 : # 블록갯수가 4가 넘으면 터지는 것
                bomb_cnt += 1 # 터지는 블록 카운트

            if cnt > max_cnt :
                max_cnt = cnt
print(bomb_cnt, max_cnt)