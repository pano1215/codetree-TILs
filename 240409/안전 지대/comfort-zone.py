import sys

sys.setrecursionlimit(10**5)

# 입력값 받기 
n, m = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(n)]
village_copy = [num[:] for num in village] # village를 계속 이용할 것이기 때문에(k이하는 0으로 바꿔줘야하니까) copy배열 만들기 
visited = [[False for _ in range(m)] for _ in range(n)] # 방문 배열 만들기(초기화 상태)
k = 1 # 비 높이 선언

# 최대 건물 높이 선언
max_height = -sys.maxsize
for row in range(n) :
    height = max(village[row])
    if height > max_height :
        max_height = height

# 격자 안에서 벗어나는지 아닌지 체크하는 함수
def is_in_range(next_x, next_y) :
    return 0 <= next_x < n and 0 <= next_y < m

# dfs를 반복하면서 0인 곳은 방문 불가로 처리함
def dfs(x, y) :
    global cnt

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    if village_copy[x][y] != 0 :
        # 이미 방문한 곳은 visted에서 True로 처리해서 방문하지 못하도록 함
        visited[x][y] = True
        village_copy[x][y] = 0
        
        # 네 방향 중에 전진 가능한 곳을 재호출 
        for dx, dy in zip(dxs, dys) :
            # next_x, next_y 세팅
            next_x = x + dx
            next_y = y + dy

            if is_in_range(next_x, next_y) and village_copy[next_x][next_y] != 0 :
                dfs(next_x, next_y)
    
    # 다음 위치의 값이 0이 아닌 경우에 이동
    # if village_copy[x][y] != 0 :
    #     # 이미 방문한 곳은 visted에서 True로 처리해서 방문하지 못하도록 함
    #     visited[x][y] = True
    #     village_copy[x][y] = 0
    #     cnt += 1

    #     print(k, cnt)
    #     print(village_copy)
    #     ## 네 방향 중에 전진 가능한 곳을 재호출 
    #     for dx, dy in zip(dxs, dys) :
    #         # next_x, next_y 세팅
    #         next_x = x + dx
    #         next_y = y + dy

    #         if is_in_range(next_x, next_y) :
    #             dfs(next_x, next_y)

# k이하면 모두 0으로 처리하는 함수 
def change_to_zero_less_k(k) :
    for row in range(n) :
        for col in range(m) :
            if village_copy[row][col] <= k :
                village_copy[row][col] = 0
    #print(k, village_copy)
    #return village_copy

result = [] # 높이(k)와 안전지대 수를 기록할 결과 배열 만들기
# 1부터 +1씩 하면서 높이(K)를 입력해주기
while k <= max_height : # K가 최대 높이를 넘으면 종료
    cnt = 0

    # K이하면 모두 0으로 처리함
    change_to_zero_less_k(k)

    for row in range(n) :
        for col in range(m) :
            if village_copy[row][col] != 0 and visited[row][col] == False:
                dfs(row, col)
                cnt += 1
    #print(k, cnt)
    #if not a :
        # 이전 문제처럼 dfs가 끝날 때마다 cnt를 카운트해줘서 
        # 안전지대(dfs가 갈 수 있는 구역)를 체크함
    #    cnt = 0

    #print(cnt)
    # 높이(k)와 안전지대 수를 기록함 
    result.append([k, cnt])

    village_copy = [num[:] for num in village]
    visited = [[False for _ in range(m)] for _ in range(n)] # 초기화
    
    k += 1

max_cnt = -sys.maxsize
max_idx = -sys.maxsize
for row in range(len(result)) :
    k = result[row][0]
    safe_zone_cnt = result[row][1]

    # 가장 많은 안전지대 수 찾기
    if safe_zone_cnt > max_cnt :
        max_cnt = safe_zone_cnt
        max_idx = k

print(max_idx, max_cnt)