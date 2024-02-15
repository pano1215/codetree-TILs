n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1
miro = [list(str(input())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dirt = 0

r_dx = [1, 0, -1, 0]
r_dy = [0, -1, 0, 1]
r_dirt = 0

def is_in_range(temp_x, temp_y) :
    return 0 <= x < n and 0 <= y < n

def right_wall_check(temp_x, temp_y) :
    global r_dirt

    temp_x += r_dx[r_dirt]
    temp_y += r_dy[r_dirt]

    if is_in_range(temp_x, temp_y) and miro[temp_x][temp_y] == '#' : 
        #print('벽있음')
        return True 
    else :
        #print('벽없음')
        r_dirt = (r_dirt + 1) % 4
        return False 

while(miro[x][y]) :
    if x == 1 and y == 2 :
        print('여기임', right_wall_check(x, y))
    if right_wall_check(x, y) : # 벽이 있다면
        x += dx[dirt]
        y += dy[dirt]
    else :
        dirt = (dirt + 1) % 4
        x += dx[dirt]
        y += dy[dirt]
    if not is_in_range(x, y) :
        break

    # 방문 위치를 담아두고, 해당 위치가 또 나오면 -1 출력
    
    print(dirt, x, y, miro[x][y])