n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1
miro = [list(str(input())) for _ in range(n)]













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