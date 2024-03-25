n, m = tuple(map(int, input().split()))
cnt = 0

# 간선배열 만들기
arr = [[0 for _ in range(n)] for _ in range(n)]

# 방문배열 만들기
visited = [False for _ in range(n)]

for i in range(m) :
    # x, y를 받아서 -1해주기
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    # x, y에 해당하는 지점 / y, x에 해당하는 지점에 1세팅
    arr[x][y] = 1
    arr[y][x] = 1

# cnt 출력
def dfs(node) :
    global cnt
    for cur_node in range(n) :
        # arr이 1이고 방문하지 않았다면 
        if arr[node][cur_node] == 1 and not visited[cur_node] :
            #방문체크
            visited[cur_node] = True
            # cnt++
            cnt += 1
            # 한 번 더 호출 
            dfs(cur_node)

# 첫 번째 노드에서 시작하기 때문에 방문으로 체크하기 
visited[0] = True
dfs(0)

print(cnt)