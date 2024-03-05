import sys

n, m = tuple(map(int, input().split()))

temp = [list(map(int, input().split())) for _ in range(n)]
arr = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr[i][j].append(temp[i][j])

# arr = [[[7, 1], [], [4]], 
#  [[2], [3], [8]], 
#  [[9], [6], [5]]]

move_arr = list(map(int, input().split()))

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

# 격자 내에 있는지 체크
def is_in_range(next_row, next_col) :
    return 0 <= next_row < n and 0 <= next_col < n

# 숫자 이동하기
def move_cur_num(a, b, c, cur_num, max_row, max_col, tar_idx, max_num) :
    temp_arr = []

    for e in arr[a][b] :
        print(a, b, arr[a][b], e, arr[a][b].pop())
        temp_arr.append(arr[a][b].pop())

    for e in arr[max_row][max_col] :
        temp_arr.append(arr[max_row][max_col].pop())
        #print('temp_arr : ', temp_arr)

    arr[max_row][max_col] = temp_arr
    if len(arr[a][b]) == 0 :
        arr[a][b].append(0)
    
    print(arr)


# 8방향 중에서 가장 큰 수가 있는지 체크
def find_the_biggest_num(row, col, point) :
    max_num = -sys.maxsize
    tar_idx = -1
    global move_num
    
    for dx, dy in zip(dxs, dys) :
        next_row = row + dx
        next_col = col + dy

        if is_in_range(next_row, next_col) :
            for e in arr[next_row][next_col] :
                if e >= max_num :
                    max_num = e
                    max_row = next_row
                    max_col = next_col
                    tar_idx = arr[next_row][next_col].index(e)
    return max_row, max_col, tar_idx, max_num
    print(row, col, point, max_num, tar_idx)

# 움직일 숫자의 위치 찾기
def find_point(arr, move_num) :
    for a in range(len(arr)) :
        for b in range(len(arr[a])) :
            for c in range(len(arr[a][b])) :
                if arr[a][b][c] == move_num :
                    #print(a, b, c, move_num, arr)
                    return a, b, c

for i in range(len(move_arr)) :
    a, b, c = find_point(arr, move_arr[i])
    if move_arr[i] == arr[a][b][c] :
        # 8방향 중에서 제일 큰 숫자의 위치 리턴
        max_row, max_col, tar_idx, max_num = find_the_biggest_num(a, b, c) 
        move_cur_num(a, b, c, arr[a][b][c], max_row, max_col, tar_idx, max_num)
        
# # 현재 숫자를 새로운 곳으로 이동
# def move_cur_num(row, col, temp) :
#     next_num = temp[0]
#     next_row = temp[1]
#     next_col = temp[2]

#     now_num = arr[row][col]
#     arr[row][col] = 0
#     arr[next_row][next_col] = []

#     arr[next_row][next_col].append(now_num)
#     arr[next_row][next_col].append(next_num)
    
#     print(arr)

# for move_num in move_arr :
#     for i, e in enumerate(arr) :
        
#         try :
#             row = i
#             col = e.index(move_num)
#             # print(i, e.index(move_num), move_num)

#             find_the_biggest_num(row, col)
#         except:
#             try : 
#                 for ii, ee in enumerate(e) :
#                     row = ii
#                     col = ee.index(move_num)
                    
#                     # if move_num == 7 :
#                     #     print('move_num : 7 ', ii, ee.index(move_num))        
#                     find_the_biggest_num(row, col)
#             except:
#                 continue