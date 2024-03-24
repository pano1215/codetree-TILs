import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 폭탄의 위치
bomb_pos = []
for row in range(n) :
    for col in range(n) :
        if arr[row][col] == 1 :
            bomb_pos.append([row, col])

# 폭탄이 터지는 범위 
bomb_range = {
    1 : [[-2, 0], [-1, 0], [1, 0], [2,0]]
    , 2 : [[0, 1], [1, 0], [0, -1], [-1, 0]]
    , 3 : [[-1, 1], [1, 1], [1, -1], [-1, -1]]
}

bomb_arr = [] # 폭탄의 숫자 조합을 만드는 배열
max_num = -sys.maxsize

# 터지는 곳의 갯수를 체크
def count_detonate_num(copy_arr) :
    global max_num

    bomb_cnt = 0
    for row in range(len(copy_arr)) :
        for col in range(len(copy_arr)) :
            if copy_arr[row][col] == 1 :
                bomb_cnt += 1
    return bomb_cnt

# 격자 범위 체크 함수
def is_in_range(next_row, next_col) :
    return 0 <= next_row < n and 0 <= next_col < n

# 폭탄 터트리기 
def detonate_bomb(bomb_type_pos) :
    copy_arr = [[0 for _ in range(n)] for _ in range(n)]
    
    for bomb_row in range(len(bomb_pos)) :
        row = bomb_type_pos[bomb_row][0]
        col = bomb_type_pos[bomb_row][1]
        b_type = bomb_type_pos[bomb_row][2]

        move_arr = bomb_range[b_type]
        copy_arr[row][col] = 1 # 폭탄이 있는 위치도 터져야 함으로 1로 세팅
        for i in range(4) :
            next_row = row + move_arr[i][0]
            next_col = col + move_arr[i][1]

            if is_in_range(next_row, next_col) :
                copy_arr[next_row][next_col] = 1
    #print(copy_arr)
    return count_detonate_num(copy_arr)

# 폭탄 넘버와 폭탄 위치를 매칭시킴 : 첫 번째 row, col은 첫 번째 폭탄
def find_bomb_point(bomb_arr, bomb_pos) :
    bomb_type_pos = [[0 for _ in range(len(bomb_pos[row]))] for row in range(len(bomb_pos))]
    
    for row in range(len(bomb_pos)) :
        for col in range(len(bomb_pos[row])) :
            bomb_type_pos[row][col] = bomb_pos[row][col]
        bomb_type_pos[row].append(bomb_arr[row])
    #print(bomb_type_pos)
    return detonate_bomb(bomb_type_pos)

# 폭탄 터트리는 조합 만들기 
def bomb_goes_off(num) :
    global bomb_cnt

    if len(bomb_arr) >= len(bomb_pos) :
        # 이 부분에서 폭탄 터지는 위치 구하기 
        if len(bomb_arr) == len(bomb_pos) :
            bomb_cnt = find_bomb_point(bomb_arr, bomb_pos) # 폭탄 종류와 폭탄 위치 합치기
            return bomb_cnt
        return 0

    max_ans = 0
    for i in range(1, 4) : # 1번부터 3번까지의 폭탄을 의미함 
        bomb_arr.append(i)
        #print(bomb_arr)
        max_ans = max(max_ans, bomb_goes_off(num + 1))
        bomb_arr.pop()
    return max_ans

print(bomb_goes_off(0))