import sys

# 선언부
n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r_c = [list(map(int, input().split())) for _ in range(m)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

count = [[0 for _ in range(n)] for _ in range(n)] 
next_count = [[0 for _ in range(n)] for _ in range(n)] 

# 배열 범위 체크 함수
def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 구슬 위치 기록 함수 
def Record(count_arr) :
    for i in range(m) :
        r = r_c[i][0] - 1
        c = r_c[i][1] - 1

        count_arr[r][c] = 1
    return count_arr

# 상하좌우 최댓값 탐색
def Check(row, col) :
    global max_x, max_y
    max_num = - sys.maxsize

    for dx, dy in zip(dxs, dys) :
        next_x, next_y = row + dx, col + dy
        if is_in_range(next_x, next_y) and max_num < arr[next_x][next_y] :
            max_num = arr[next_x][next_y]
            max_x = next_x
            max_y = next_y

    return max_x, max_y

# next_count를 count배열에 복사
def Copy(next_count) :
    for i in range(n) :
        for j in range(n) :
            count[i][j] = next_count[i][j]
    return count

# count에서 요소가 2이상인 것 0으로 제거
def Check_two(count) :
    for i in range(n) :
        for j in range(n) :
            if count[i][j] >= 2 :
                count[i][j] = 0
    return count

# 요소가 1인 것의 갯수 세기
def Check_one(count) :
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if count[i][j] == 1 :
                cnt += 1
    return cnt

# count배열에 구슬 위치 기록
count = Record(count)

for tt in range(t) :
    for row in range(n) :
        for col in range(n) :
            if count[row][col] != 0 :
                max_row, max_col = Check(row, col)
                next_count[max_row][max_col] += 1
            else :
                continue

    count = Copy(next_count)
    #print(tt, ', Copy(next_count) :', count)
    count = Check_two(count)
    #print(tt, ', Check_two(count) :', count)

cnt = Check_one(count)
print(cnt)


# visited_arr = []

# def Check(r, c) :
#     cur_num = arr[r][c]
#     for dx, dy in zip(dxs, dys) :
#         next_x, next_y = r + dx, c + dy

#         if is_in_range(next_x, next_y) and cur_num < arr[next_x][next_y] :
#             return next_x, next_y

# for _ in range(t) :
#     for i in range(m) :
#         r = r_c[i][0] - 1
#         c = r_c[i][1] - 1

#         print(Check(r, c))
        # if [max_x, max_y] not in visited_arr: # 처음 등장한 원소
        #     visited_arr.append([max_x, max_y])
        # else:
        #     continue
            
# print(max_x, max_y)
# print(visited_arr)
#print(len(visited_arr))