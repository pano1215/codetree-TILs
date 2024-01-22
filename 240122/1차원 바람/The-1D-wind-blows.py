n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
wind = [list(map(str, input().split())) for _ in range(q)]

# 배열 범위 체크 함수
def row_plus_in_range(x):
    return 0 <= x < n 

# 배열 범위 체크 함수
def row_mius_in_range(x):
    return 0 <= x < n 

def Up_check(row, arr) :
    check = False
    for j in range(m) :
        if row_mius_in_range(row - 1) and arr[row - 1][j] == arr[row][j] :
            check = True
    return check

def Down_check(row, arr) :
    check = False
    for j in range(m) :
        if row_plus_in_range(row + 1) and arr[row + 1][j] == arr[row][j] :
            check = True
    return check

def Left_move(row) :
    last_temp = arr[row][-1] 
    
    for i in range(m - 1, 0, -1) :
        arr[row][i] = arr[row][i - 1]
    arr[row][0] = last_temp
    return arr

def Move(row, dirt) :
    if dirt == 'L' :
        last_temp = arr[row][-1]
        for i in range(m - 1, 0, -1) :
            arr[row][i] = arr[row][i - 1]
        arr[row][0] = last_temp
    else :
        first_temp = arr[row][0]
        for i in range(1, m) :
            arr[row][i] = arr[row][i + 1]
        arr[row][-1] = first_temp
    return arr

def Right_move(row) :
    first_temp = arr[row][0] 
    for i in range(1, m) :
        arr[row][i] = arr[row][i + 1]
    arr[row][-1] = first_temp
    return arr

for i in range(q) :
    row = int(wind[i][0]) - 1
    dirt = wind[i][1] 
    
    arr = Move(row, dirt)
    #if dirt == 'L' :
    #    arr = Left_move(row) 
    #    dirt == 'R'
    #else :
    #    arr = Right_move(row) 
    #    dirt == 'L'

    if Up_check(row, arr) and Down_check(row, arr) :
        print('둘 다 true')
    elif Up_check(row, arr) :
        print('Up_check true')
    elif Down_check(row, arr) :
        print('Down_check true')
    else :
        print('둘 다 false')

# print(arr)