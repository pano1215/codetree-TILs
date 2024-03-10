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

cnt = 0
heaviest = 0 

# 남은 구슬 개수 & 가장 무거운 구슬 무게 구하기
def remaining_num_weight_heaviest(miro) :
    global cnt, heaviest

    for line in miro :
        for ee in line :
            if len(ee) > 0 :
                cnt += 1

                weight = ee[3] 

                if weight > heaviest :
                    heaviest = weight
    return cnt, heaviest
            
            

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

    wght = 0
    turn_num = 0

    next_row = row + dxs[dirt]
    next_col = col + dys[dirt]

    # if (row == 0 and col == 0) or (row == 0 and col == 2) :
    #     print(next_row, next_col, dirt, dxs[dirt], dys[dirt])

    if is_in_range(next_row, next_col) :
        if len(miro[next_row][next_col]) > 0 : # 이동할 위치(miro[next_row][next_col])에 값이 있는 경우
            # 무게랑 순서 뽑기
            wght = miro[next_row][next_col][3]
            turn_num = miro[next_row][next_col][4]
            miro[next_row][next_col] = [] # 이동할 []

        miro[next_row][next_col].append(next_row)
        miro[next_row][next_col].append(next_col)
        miro[next_row][next_col].append(dirt)
        miro[next_row][next_col].append(weight + wght)

        if turn_num > index :
            miro[next_row][next_col].append(turn_num)
        else :
            miro[next_row][next_col].append(index)

        #print(miro[row][col])
        if len(miro[row][col]) > 0 : # 이동한 위치(miro[row][col])에 값이 있는 경우
            miro[row][col] = [] # 이동한 []
    else : # 격자에서 벗어난 경우
        dirt = change_dirt(dirt) 

        miro[row][col][2] = dirt # 위치는 그대로이기 때문에 방향만 바꿔줌

        #if len(miro[row][col]) > 0 : # 이동한 위치(miro[row][col])에 값이 있는 경우
        #    miro[row][col] = [] # 이동한 []
    return miro

# t초 동안 움직이기
for time in range(t) :
    for turn in range(m + 1) : # 구슬의 순서대로 이동시키기 위함
        check = False # 구슬이 한 번 이동했는지 체크하기 위한 변수 
        for i in range(n) : 
            for j in range(n) :
                if len(miro[i][j]) == 0 : # 구슬이 없는 경우 패스
                    continue

                # 구슬이 있는 경우에 아래 로직 실행    
                if miro[i][j][4] == turn : 
                    # 구슬의 순서대로 
                    miro = move(miro[i][j])
                    check = True
                if check : 
                    break
            if check : 
                break
#print(miro) 

# 남은 구슬 개수 & 가장 무거운 구슬 무게 구하기
cnt, heaviest = remaining_num_weight_heaviest(miro)
print(cnt, heaviest)