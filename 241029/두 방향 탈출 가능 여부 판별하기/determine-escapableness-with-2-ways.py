n, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
escape_result = -1

def is_range(next_x, next_y) :
    return 0 <= next_x < n and 0 <= next_y < m

def can_do(next_x, next_y) :
    # visited False 이고 miro 1인 경우
    return is_range(next_x, next_y) and not visited[next_x][next_y] and miro[next_x][next_y] == 1

def escape_yes_no(next_x, next_y) :
    return next_x == n - 1 and next_y == n - 1

def dfs(x, y) :
    global escape_result

    dxs = [0, 1]
    dys = [1, 0]

    for dx, dy in zip(dxs, dys) :
        next_x, next_y = x + dx, y + dy
        
        if can_do(next_x, next_y) :
            miro[next_x][next_y] = -1
            visited[next_x][next_y] = True
            dfs(next_x, next_y)

            escape_result = escape_yes_no(next_x, next_y)
            #print('can_do 호출해서 True 나옴')

visited[0][0] = True
dfs(0, 0)

if escape_result : 
    print(1)
else :
    print(0)