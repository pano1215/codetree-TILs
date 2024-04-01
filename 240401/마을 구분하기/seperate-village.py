n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)] # 사람 | 벽 배열
visited = [[False for _ in range(n)] for _ in range(n)] # 방문체크 배열 
section = [] # 마을 정보를 담을 배열 

# 벽이 있는 곳은 방문을 못하게 하기 위해 True로 처리하기
for row in range(n) :
    for col in range(n) :
        if arr[row][col] == 0 :
            visited[row][col] = True

# 격자 안에서 벗어나는지 아닌지 체크하는 함수
def is_in_range(next_x, next_y) :
    return 0 <= next_x < n and 0 <= next_y < n

# dfs 
def dfs(x, y) :
    #print('x, y : ', x, y)
    global cnt 

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    # [현재x][현재y]가 1이면 -> 방문 체크 & cnt += 1 & 방문한 곳에 2로 찍기
    if arr[x][y] == 1 :
        visited[x][y] = True
        arr[x][y] = 2 
        cnt += 1

        ## 네 방향 중에 1인 곳을 파라미터로 재호출
        for dx, dy in zip(dxs, dys) :
            # next_x, next_y 세팅
            next_x = x + dx
            next_y = y + dy

            if is_in_range(next_x, next_y) :
                dfs(next_x, next_y)
    #print(cnt, arr)

cnt = 0 
for row in range(n) :
    for col in range(n) :
        if arr[row][col] == 1 :
            a = dfs(row, col)
            if not a :
                #print(cnt, a)
                section.append(cnt) 
                cnt = 0

for e in range(len(section) * 2) :
    if 0 in section :
        section.remove(0)
section.sort()

print(len(section))

for e in section :
    print(e)