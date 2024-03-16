import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
copy_arr = [i[:] for i in arr]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

delete_row_col = []
cnt = 0 # 쌍의 개수 세기 
max_num = -sys.maxsize

# 격자 범위 체크 함수
def is_in_range(next_row, next_col) :
    return 0 <= next_row < n and 0 <= next_col < n

#다시 완전탐색하며 쌍을 이룬 케이스를 카운트한다
def find_fair(copy_arr) : 
    global cnt 
    cnt = 0 

    for row in range(len(copy_arr)) : 
        for col in range(len(copy_arr)) : 
            # 값이 0이면 비어있는 것이니 패스하기
            if copy_arr[row][col] == 0 :
                continue 

            for dirt in range(0, 4) : 
                next_row = row + dxs[dirt]
                next_col = col + dys[dirt] 

                if is_in_range(next_row, next_col) :
                    if copy_arr[row][col] == copy_arr[next_row][next_col] :
                        cnt += 1
    cnt /= 2
    cnt = int(cnt)
    #print(cnt)
    return cnt

# 다른 배열(next_arr)의 숫자를 원래 배열(copy_arr)로 옮겨 담는다
def move_copy_arr(next_arr) :
    global copy_arr 

    # copy_arr 배열 초기화
    copy_arr = [[0 for _ in range(n)] for _ in range(n)]

    for row in range(len(next_arr)) :
        if len(next_arr[row]) == 0 :
            continue
        for col in range(len(next_arr[row])) :
            copy_arr[len(copy_arr) - 1 - col][row] = next_arr[row][col]
    #print(copy_arr)
    return find_fair(copy_arr)

#삭제 후 남은 숫자를 다른 배열(next)에 옮긴다 
def move_next_arr(copy_arr) :
    next_arr = [[] for _ in range(n)]

    for row in range(n) :
        for col in range(n) :
            if copy_arr[col][row] == 0 :
                continue
            else :
                next_arr[row].append(copy_arr[col][row])
        next_arr[row].reverse()
    #print(next_arr)
    return move_copy_arr(next_arr)

#삭제할 [row, col]에 따라 삭제한다
def delete_row_col_finc(delete_row_col) :
    global copy_arr
    copy_arr = [i[:] for i in arr]

    for i in range(len(delete_row_col)) :
        row = delete_row_col[i][0]
        col = delete_row_col[i][1]

        copy_arr[row][col] = 0
    #print(copy_arr)
    return move_next_arr(copy_arr)

# 폭탄 선정해서 삭제할 [row, col]만들기 - tar_num 폭탄 범위 수 
def create_delete_row_col(row, col) :
    global delete_row_col
    delete_row_col = [[row, col]]

    ori_row, ori_col = row, col
    for dirt in range(0, 4) : 
        row, col = ori_row, ori_col
        for i in range(arr[row][col] - 1) :
            next_row = row + dxs[dirt]
            next_col = col + dys[dirt] 

            if is_in_range(next_row, next_col) :
                delete_row_col.append([next_row, next_col])
            row, col = next_row, next_col
    #print(ori_row, ori_col, delete_row_col)
    return delete_row_col_finc(delete_row_col)   

#배열의 모든 번호를 완전 탐색한다
for row in range(n) :
    for col in range(n) :
        #모든 번호가 적힌 숫자대로 폭탄을 터트린다(이때 삭제할 [row, col]만들기)
        pair_num = create_delete_row_col(row, col)

        #이 과정을 반복하며 가장 많은 쌍을 만드는 숫자를 고른다 
        if pair_num > max_num :
            max_num = pair_num

print(max_num)