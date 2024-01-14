# for r in range(row) : # row 순회
#     for c in range(column) : # column 순회
#         while x >= 0 and x < row and y >= 0 and y < column :

import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]

def is_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < n

max_num = -sys.maxsize
for row in range(n) : 
    for column in range(n) :
        # route_sum = 0
        # temp_x = arr[row][column]
        # rr = row
        # cc = column

        for upper in range(1, n) : # 가로길이
            for height in range(1, n) : # 세로길이
                move_nums = [upper, height, upper, height]
                temp_x = 0 

                for dx, dy, move_num in zip(dxs, dys, move_nums):
                    for _ in range(move_num) :
                        row, column = row + dx, column + dy
                        if is_range(row, column) :
                            temp_x += arr[row][column]
                        else :
                            continue ;
                max_num = max(max_num, temp_x)
print(max_num)

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