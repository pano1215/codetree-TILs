# 입력
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 선언
r -= 1
c -= 1

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

delete_num = arr[r][c] 
arr[r][c] = 0

# 격자 범위 체크
def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# temp를 arr에 합치기
def Gether(temp, col) :
    cnt = 0 # temp와의 길이를 넘을 경우엔 0으로 삽입하기 위함
    leng_temp = len(temp)
    for i in range(n - 1, -1, -1) :
        if cnt < leng_temp :
            arr[i][col] = temp[-1]
            temp = temp[:-1]
            #print('col-Gether-temp : ', col, temp)
        else : 
            arr[i][col] = 0
        cnt += 1
    return arr

# 폭탄이 터진 후 블록을 내려주기
def Move(arr) :
    #temp = [[0 for _ in range(n)] for _ in range(n)]
    #print(temp)
    for j in range(n) :
        temp = []
        for i in range(n - 1, -1, -1) :
            if arr[i][j] != 0 :
                temp.append(arr[i][j])
        temp.reverse()
        #print('j, temp : ', j, temp)
        arr = Gether(temp, j) 
        #print(arr)
    return arr

# 폭탄 터짐 - 네 방향을 탐색하며 0으로 바꿔주는 함수
def Change_zero(r, c) :
    ori_r, ori_c = r, c
    for dx, dy in zip(dxs, dys) :
        for step in range(delete_num - 1) :
            next_x = r + dx
            next_y = c + dy

            if is_in_range(next_x, next_y) :
                arr[next_x][next_y] = 0

                r = next_x
                c = next_y
        r, c = ori_r, ori_c
    #print('ARR : ', arr)
    return Move(arr)

arr = Change_zero(r, c)

for e in arr :
    for ee in e :
        print(ee, end = ' ')
    print()