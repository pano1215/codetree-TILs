n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1
miro = [list(str(input())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dirt = 0

def is_in_range() :
    return 0 <= x < n and 0 <= y < n

def right_wall_check(x, y) :
    if miro[x + 1][y] == '#' : 
        return True #'벽있음')
    else :
        return False # print('벽없음')

while(miro[x][y]) :
    if right_wall_check(x, y) : # 벽이 있다면
        x += dx[dirt]
        y += dy[dirt]
    else :
        dirt = (dirt + 1) % 4
        x += dx[dirt]
        y += dy[dirt]
    print(dirt, x, y, miro[x][y])