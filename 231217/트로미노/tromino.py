import sys

row, column = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]

#     ㄴ        ㄱ       ㅢ       ㅣㅡ     ㅣ        ㅡ
dx = [0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 2, 0, 0, 0]
dy = [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 2]

def in_range(x, y) :
    return x >= 0 and x < row and y >= 0 and y < column

max_num = -sys.maxsize
for r in range(row) :
    for c in range(column) :
        sum_temp = 0
        for xy in range(len(dx)) :
            if xy % 3 == 0 :
                sum_temp = 0

            if in_range(r + dx[xy], c + dy[xy]):
                sum_temp += arr[r + dx[xy]][c + dy[xy]]
                #print(r + dx[xy], c + dy[xy], sum_temp)
            max_num = max(max_num, sum_temp)
            
print(max_num)