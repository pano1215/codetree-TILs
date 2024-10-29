n, m = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]
visited = [False for _ in range(n)]
cnt = 0 # 횟수

# 좌표입력받아서 1로 체크하기
for _ in range(m) :
    x, y = map(int, input().split())

    # 배열에 맞게 -1 해주기
    x -= 1
    y -= 1

    arr[x][y] = 1
    arr[y][x] = 1

def dfs(curr) :
    global cnt

    for col in range(len(arr[curr])) :
        if arr[curr][col] == 1 and not visited[col] :
            visited[col] = True
            print(curr, col, visited)
            cnt += 1
            dfs(col)

visited[0] = True
dfs(0)

print(cnt)