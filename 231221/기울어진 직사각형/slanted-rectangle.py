# for r in range(row) : # row 순회
#     for c in range(column) : # column 순회
#         while x >= 0 and x < row and y >= 0 and y < column :

import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def is_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < n

max_num = -sys.maxsize
for row in range(n) :
    for column in range(n) :
        route_sum = 0
        temp_x = 0
        for upper in range(1, n) :
            for height in range(1, n) :
                if route_sum == 0 :
                    if is_range(row - upper, column - upper) :
                        temp_x += arr[row - upper][column - upper]
                elif route_sum == 1 :
                    if is_range(row + upper, column - upper) :
                        temp_x += arr[row + upper][column - upper]
                elif route_sum == 2 :
                    if is_range(row + upper, column + upper) :
                        temp_x += arr[row + upper][column + upper]
                elif route_sum == 3 :
                    if is_range(row - upper, column + upper) :
                        temp_x += arr[row - upper][column + upper]

                route_sum = (route_sum + 1) % 4
        max_num = max(max_num, temp_x)
print(max_num)