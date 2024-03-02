import sys

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move_arr = list(map(int, input().split()))

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

# 격자 내에 있는지 체크
def is_in_range(next_row, next_col) :
    return 0 <= next_row < n and 0 <= next_col < n

# 현재 숫자를 새로운 곳으로 이동
def move_cur_num(row, col, temp) :
    next_num = temp[0]
    next_row = temp[1]
    next_col = temp[2]

    now_num = arr[row][col]
    arr[row][col] = 0
    arr[next_row][next_col] = []

    arr[next_row][next_col].append(now_num)
    arr[next_row][next_col].append(next_num)
    
    print(arr)

# 8방향 중에서 가장 큰 수가 있는지 체크
def find_the_biggest_num(row, col) :
    max_num = -sys.maxsize
    global move_num
    
    for dx, dy in zip(dxs, dys) :
        next_row = row + dx
        next_col = col + dy

        if is_in_range(next_row, next_col) :
            try :
                if arr[next_row][next_col] >= max_num :

                    temp = []
                    max_num = arr[next_row][next_col]
                
                    temp.append(max_num)
                    temp.append(next_row)
                    temp.append(next_col)
            except: 
                print('에러가 나나', next_row, next_col)
            print('시작', move_num, temp)
    # print(arr[row][col], temp)
    if move_num == 7 :
        print('move_num : 7 ', max_num, temp)
    move_cur_num(row, col, temp)

for move_num in move_arr :
    for i, e in enumerate(arr) :
        
        try :
            row = i
            col = e.index(move_num)
            # print(i, e.index(move_num), move_num)

            find_the_biggest_num(row, col)
        except:
            try : 
                for ii, ee in enumerate(e) :
                    row = ii
                    col = ee.index(move_num)
                    
                    # if move_num == 7 :
                    #     print('move_num : 7 ', ii, ee.index(move_num))        
                    find_the_biggest_num(row, col)
            except:
                continue