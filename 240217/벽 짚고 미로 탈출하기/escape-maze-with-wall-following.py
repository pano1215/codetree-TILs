n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1
miro = [list(str(input())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dirt = 0

# 현재 위치
cur_point = miro[x][y]

def is_in_range(right_x, right_y) :
    return 0 <= right_x < n and 0 <= right_y < n

# 회전을 여러 번 할 경우 - 위치 체크 함수
def same_diff_dirt_check(x, go_x, y, go_y, dirt) :
    while True :
        if x == go_x and y == go_y : 
            dirt, go_x, go_y = move_and_block_check(x, y, dirt)
            
        if x != go_x or y != go_y : 
            return dirt, go_x, go_y

# 이동할 위치에 따라 방향 설정 & 이동
def move_and_block_check(x, y, dirt) :
    # 전진할 좌표 설정
    go_x = x + dx[dirt]
    go_y = y + dy[dirt]
    if is_in_range(go_x, go_y) and miro[go_x][go_y] == '#' :
        #print('전진할 곳에 벽 있음')

        # 반시계 방향 설정
        dirt = (dirt + 3) % 4
        #print('반시계 방향 설정 : ', dirt)

        # 이동을 하지 않기 때문에 원래 위치 리턴, 바뀐 방향 리턴
        return dirt, x, y
            
    elif is_in_range(go_x, go_y) and miro[go_x][go_y] == '.' :
        #print('전진할 곳에 벽 없음')
        cur_point = miro[go_x][go_y]
        #print('전진할 곳으로 전진함 : ', go_x, go_y)
        # 이동하기 때문에 이동할 위치 리턴, 원래 방향 리턴
        return dirt, go_x, go_y
    elif not is_in_range(go_x, go_y) : # 격자에서 벗어나는 경우
        return dirt, go_x, go_y # 벗어난 위치를 리턴

# 오른쪽에 벽이 있는지 없는지 체크
def right_wall_check(x, y, dirt) :
    
    global go_x, go_y 

    # 오른쪽 방향 설정
    right_dirt = (dirt + 1) % 4

    right_x = x + dx[right_dirt] 
    right_y = y + dy[right_dirt] 

    if is_in_range(right_x, right_y) and miro[right_x][right_y] == '#' :
        #print('오른쪽에 벽 있음')
        #print('move_and_block_check 실행')
        dirt, go_x, go_y = move_and_block_check(x, y, dirt)

        dirt, go_x, go_y = same_diff_dirt_check(x, go_x, y, go_y, dirt)

    elif is_in_range(right_x, right_y) and miro[right_x][right_y] == '.' :
        #print('오른쪽에 벽 없음')

        # 시계방향으로 90도 회전함
        dirt = (dirt + 1) % 4

        #print('move_and_block_check 실행')
        dirt, go_x, go_y = move_and_block_check(x, y, dirt)

        dirt, go_x, go_y = same_diff_dirt_check(x, go_x, y, go_y, dirt)

    else : # 격자를 벗어나는 경우
        return dirt, go_x, go_y 
    
    return dirt, go_x, go_y 

cnt = 0

# 방문한 곳 저장 
visited = []
while True :
    dirt, x, y = right_wall_check(x, y, dirt)
    cnt += 1

    if not is_in_range(x, y) :
        break

    if [x, y, dirt] in visited :
        cnt = -1
        break
    
    visited.append([x, y, dirt])

print(cnt)
#print('dirt, x, y, cnt : ', dirt, x, y, cnt)

###############################################
# ccw_dx = [0, -1, 0, 1]
# ccw_dy = [1, 0, -1, 0]
# ccw_dirt = 0

# ccw_r_dx = [1, 0, -1, 0]
# ccw_r_dy = [0, 1, 0, -1]
# ccw_r_dirt = 0

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# dirt = 0

# r_dx = [1, 0, -1, 0]
# r_dy = [0, -1, 0, 1]
# r_dirt = 0

# def is_in_range(temp_x, temp_y) :
#     return 0 <= x < n and 0 <= y < n

# def right_wall_check(temp_x, temp_y) : # 오른쪽에 벽이 있는지 체크
#     global r_dirt

#     print('첫 번째 : ', temp_x, temp_y)
#     temp_x += ccw_r_dx[ccw_r_dirt]
#     temp_y += ccw_r_dy[ccw_r_dirt]
#     print('두 번째 : ', temp_x, temp_y, ccw_r_dirt)

#     if is_in_range(temp_x, temp_y) and miro[temp_x][temp_y] == '#' : 
#         #print('벽있음')
#         return True 
#     else :
#         print('벽없음')
#         ccw_r_dy = (ccw_r_dy + 1) % 4
#         return False

# cnt = 0
# while True :
#     if right_wall_check(x, y) : # 벽이 있다면 
#         # 전진
#         x += ccw_dx[ccw_dirt]
#         y += ccw_dy[ccw_dirt]
#         if is_in_range(x, y) and miro[x][y] == '#' : # 가려는 곳에 또 벽이 있는 경우 
#             # 위치 원복
#             x -= ccw_dx[ccw_dirt]
#             y -= ccw_dy[ccw_dirt]
#             ccw_dirt = (ccw_dirt + 1) % 4
#     else :
#         ccw_dirt = (ccw_dirt + 1) % 4
#         print('벽없음 dirt : ', ccw_dirt)
#         x += ccw_dx[ccw_dirt]
#         y += ccw_dy[ccw_dirt]

    
#     if not is_in_range(x, y) :
#         break

#     print(dirt, x, y, miro[x][y])

#     cnt += 1
    
# print(cnt)