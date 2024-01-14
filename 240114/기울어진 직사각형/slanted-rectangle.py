# for r in range(row) : # row 순회
#     for c in range(column) : # column 순회
#         while x >= 0 and x < row and y >= 0 and y < column :

import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def is_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < n

def get_score(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]
    
    sum_of_nums = 0

    # 기울어진 직사각형의 경계를 쭉 따라가봅니다.
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy
                
            # 기울어진 직사각형이 경계를 벗어나는 경우라면
            # 불가능하다는 의미로 답이 갱신되지 않도록
            # 0을 반환합니다.
            if not is_range(x, y):
                return 0
            
            sum_of_nums += arr[x][y]
    
    return sum_of_nums

max_num = -sys.maxsize

for row in range(n) : 
    for column in range(n) :
        # route_sum = 0
        # temp_x = arr[row][column]
        # rr = row
        # cc = column

        for upper in range(1, n) : # 가로길이
            for height in range(1, n) : # 세로길이
                max_num = max(max_num, get_score(row, column, upper, height))
print(max_num)
                # move_nums = [upper, height, upper, height]
                # dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
                # temp_x = 0 
                # boolean = False

                # for dx, dy, move_num in zip(dxs, dys, move_nums):
                #     for _ in range(move_num) :
                #         row, column = row + dx, column + dy
                        
                #         if is_range(row, column) :
                #             temp_x += arr[row][column]
                #             #print(row, column, upper, height)
                #         else :
                #             row, column = row - dx, column - dy
                #             temp_x = 0
                #             print('111111111111111111111111111111111111111')
                #             continue 
                

                # route_sum = 0
                # temp_x = arr[rr][cc]
                # rr = row
                # cc = column
                # while route_sum < 4 : # 방향을 4번 바꿔야함 (0 > 1 > 2 > 3 순서로 이동)
                #     if route_sum == 0 : 
                #         for up in range(upper) : # 1부터 가로길이까지의 합 구하기
                #             if is_range(row - up, column - up) :
                #                 temp_x += arr[row - up][column - up]
                #             else :
                #                 break
                        
                #         rr -= upper
                #         cc -= upper

                #     elif route_sum == 1 :
                #         for hgt in range(height) : # 1부터 세로길이까지의 합 구하기
                #             if is_range(rr + hgt, cc - hgt) :
                #                 temp_x += arr[rr + hgt][cc - hgt]
                #             else :
                #                 break
                        
                #         rr += height
                #         cc -= height

                #     elif route_sum == 2 :
                #         for up in range(upper) : # 1부터 가로길이까지의 합 구하기
                #             if is_range(rr + up, cc + up) :
                #                 temp_x += arr[rr + up][cc + up]
                #             else :
                #                 break

                #         rr += upper
                #         cc += upper

                #     elif route_sum == 3 :
                #         for hgt in range(height) : # 1부터 세로길이까지의 합 구하기
                #             if is_range(rr - hgt, cc + hgt) :
                #                 temp_x += arr[rr - hgt][cc + hgt]
                #             else :
                #                 break

                #         rr -= height
                #         cc += height

                #     route_sum = route_sum + 1
                # if temp_x == 20 :
                #     print(row, column, upper, height)