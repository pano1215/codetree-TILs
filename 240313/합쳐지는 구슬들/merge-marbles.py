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

# 격자 범위 체크 함수
def is_in_range(next_row, next_col) :
    return 0 <= next_row < n and 0 <= next_col < n

# 남은 구슬 개수 & 가장 무거운 구슬 무게 구하기
def remaining_num_weight_heaviest(miro) :
    global cnt, heaviest

    for line in miro :
        for ee in line :
            if ee[4] != 0 :
                cnt += 1

                weight = ee[3] 

                if weight > heaviest :
                    heaviest = weight
    return cnt, heaviest

# 변경된 구슬의 위치를 miro에 복사하는 함수
def copy_miro(next_miro, miro) :
    for row in range(len(next_miro)) :
        for col in range(len(next_miro)) :
            for num in range(5) :
                miro[row][col][num] = next_miro[row][col][num]
    return miro

# 격자에서 벗어나는 경우 - 방향을 전환하는 함수
def change_dirt(dirt) :
    dirt = (dirt + 2) % 4
    return dirt 

# 구슬이 이동할 위치 담기 
def move(miro) :
    global next_miro

    row = miro[0]
    col = miro[1]
    dirt = miro[2]
    weight = miro[3]
    index = miro[4]

    next_row = row + dxs[dirt]
    next_col = col + dys[dirt]

    if is_in_range(next_row, next_col) :
        # idx가 0이 아니라면 이미 움직인 구슬이 있다는 것
        if next_miro[next_row][next_col][4] != 0 :
            # idx 크기 구분하기
            if next_miro[next_row][next_col][4] > index :
                next_miro[next_row][next_col][3] += weight
            else :
                next_miro[next_row][next_col][2] = dirt
                next_miro[next_row][next_col][3] += weight
                next_miro[next_row][next_col][4] = index
        else :
            next_miro[next_row][next_col][0] = next_row
            next_miro[next_row][next_col][1] = next_col
            next_miro[next_row][next_col][2] = dirt
            next_miro[next_row][next_col][3] = weight
            next_miro[next_row][next_col][4] = index
    else : # 격자에서 벗어난 경우에는 방향만 바꾸기 
        dirt = change_dirt(dirt) 

        # idx가 0이 아니라면 이미 움직인 구슬이 있다는 것
        if next_miro[row][col][4] != 0 :
            # idx 크기 구분하기
            if next_miro[row][col][4] > index :
                next_miro[row][col][3] += weight
            else :
                next_miro[row][col][2] = dirt
                next_miro[row][col][3] += weight
                next_miro[row][col][4] = index
        else :
            next_miro[row][col][0] = row
            next_miro[row][col][1] = col
            next_miro[row][col][2] = dirt
            next_miro[row][col][3] = weight
            next_miro[row][col][4] = index
    #print('next_miro :', next_miro)
    return next_miro

# t초 동안 움직이기
for time in range(t) :
    # 이동할 구슬의 위치 담는 배열
    next_miro = [[[0 for _ in range(5)] for _ in range(n)] for _ in range(n)]

    for i in range(n) : 
        for j in range(n) :
            if len(miro[i][j]) == 0 : # 구슬이 없는 경우 패스
                continue

            next_miro = move(miro[i][j])
    miro = copy_miro(next_miro, miro)

cnt, heaviest = remaining_num_weight_heaviest(miro)
print(cnt, heaviest)