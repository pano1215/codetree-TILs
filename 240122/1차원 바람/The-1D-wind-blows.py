n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
wind = [list(map(str, input().split())) for _ in range(q)]

# 배열 범위 체크 함수 row + 1 / row - 1
def row_in_range(x):
    return 0 <= x < n 

# 배열 범위 체크 함수 row - 1
def row_mius_in_range(x):
    return 0 <= x < n 

def Up_check(row, arr) :
    #global row

    check = False
    for j in range(m) :
        if row_in_range(row - 1) and arr[row - 1][j] == arr[row][j] :
            check = True
    row = row - 1
    return check

def Down_check(row, arr) :
    #global row 

    check = False
    for j in range(m) :
        if row_in_range(row + 1) and arr[row + 1][j] == arr[row][j] :
            check = True
    row = row + 1
    return check

# def Left_move(row) :
#     last_temp = arr[row][-1] 
    
#     for i in range(m - 1, 0, -1) :
#         arr[row][i] = arr[row][i - 1]
#     arr[row][0] = last_temp
#     return arr

def Move(row, dirt) :
    if dirt == 'L' :
        last_temp = arr[row][-1]
        for i in range(m - 1, 0, -1) :

            arr[row][i] = arr[row][i - 1]
        arr[row][0] = last_temp
        dirt = 'R'
    else :
        first_temp = arr[row][0]
        for i in range(0, m - 1) :
            arr[row][i] = arr[row][i + 1]
        arr[row][-1] = first_temp
        dirt = 'L'
    return arr, dirt

# def Right_move(row) :
#     first_temp = arr[row][0] 
#     for i in range(1, m) :
#         arr[row][i] = arr[row][i + 1]
#     arr[row][-1] = first_temp
#     return arr

row = 0
for i in range(q) :
    row = int(wind[i][0]) - 1
    dirt = wind[i][1] 

    arr, dirt = Move(row, dirt)

    up_row = row
    up_dirt = dirt

    down_row = row
    down_dirt = dirt

    while(True) : # up
        if Up_check(up_row, arr) :
            up_row -= 1
            #print('Up_check true 들어가기 전 : ', up_dirt)
            arr, up_dirt = Move(up_row, up_dirt)
            #print('Up_check true : ', up_dirt)
        else :
            break
    
    while(True) : # down
        if Down_check(down_row, arr) :
            down_row += 1
            #print('Down_check true 들어가기 전 : ', down_dirt)
            arr, down_dirt = Move(down_row, down_dirt)
            #print('Down_check true : ', down_dirt)
        else :
            break

for e in  arr :
    for ee in e :
        print(ee, end = ' ')
    print()