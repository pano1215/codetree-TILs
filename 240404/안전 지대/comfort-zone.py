import sys


# dfs를 반복하면서 0인 곳은 방문 불가로 처리함
# 이미 방문한 곳은 visted에서 True로 처리해서 방문하지 못하도록 함
# 이전 문제처럼 dfs가 끝날 때마다 cnt를 카운트해줘서 
# 안전지대(dfs가 갈 수 있는 구역)를 체크함
# 가장 많은 안전지대(max_num)를 기록함
# 안전지대가 0이 되면 전체 stop(return) 

# 입력값들 받기 
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

# k이하면 모두 0으로 처리하는 함수 
def change_to_zero_less_k(k) :
    for row in range(n) :
        for col in range(m) :
            if village_copy[row][col] <= k :
                village_copy[row][col] = 0
    print(village_copy)
    return village_copy

# 1부터 +1씩 하면서 높이(K)를 입력해주기
while k <= max_height : # K가 최대 높이를 넘으면 종료
    # K이하면 모두 0으로 처리함
    village_copy = change_to_zero_less_k(k)

    k += 1