# 격자크기 구슬개수 시간
n, m, t = tuple(map(int, input().split()))

miro = [[[] for _ in range(n)] for _ in range(n)]

for idx in range(m) :
    r, c, d, w = tuple(map(str, input().split()))
    r, c, w = int(r) - 1, int(c) - 1, int(w)

    if d == 'R' :
        d = 0
    elif d == 'D' :
        d = 1
    elif d == 'L' :
        d = 2
    elif d == 'U' :
        d = 3
    
    miro[r][c].append(r)
    miro[r][c].append(c)
    miro[r][c].append(d)
    miro[r][c].append(w)
    miro[r][c].append(idx + 1)

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def is_in_range(next_row, next_col) :
    return 0 <= next_row < n and 0 <= next_col < n

# 격자에서 벗어나는 경우 - 방향을 전환하는 함수
def change_dirt(d) :
    d = (d + 2) % 4
    return d 

def move(miro_arr) :
    row = miro_arr[0]
    col = miro_arr[1]
    dirt = miro_arr[2]
    weight = miro_arr[3]
    index = miro_arr[4]

    next_row = row + dxs[dirt]
    next_col = col + dys[dirt]

    if is_in_range(next_row, next_col) :
        if len(miro[next_row][next_col]) > 0 : # 이동할 위치(miro[next_row][next_col])에 값이 있는 경우
            miro[next_row][next_col] = [] # 이동할 []

        miro[next_row][next_col].append(next_row)
        miro[next_row][next_col].append(next_col)
        miro[next_row][next_col].append(dirt)
        miro[next_row][next_col].append(weight)
        miro[next_row][next_col].append(index)

        #print(miro[row][col])
        if len(miro[row][col]) > 0 : # 이동한 위치(miro[row][col])에 값이 있는 경우
            miro[row][col] = [] # 이동한 []
    else : # 격자에서 벗어난 경우
        dirt = change_dirt(dirt) 

        miro[row][col].append(dirt) # 위치는 그대로이기 때문에 방향만 바꿔줌

        if len(miro[row][col]) > 0 : # 이동한 위치(miro[row][col])에 값이 있는 경우
            miro[row][col] = [] # 이동한 []
    return miro

# t초 동안 움직이기
for time in range(t) :
    for i in range(n) : # 격자의 *2만큼 반복
        for j in range(n) :
            if len(miro[i][j]) == 0 : # 구슬이 없는 경우 패스
                continue

            # 구슬이 있는 경우에 아래 로직 실행     
            print(move(miro[i][j]))