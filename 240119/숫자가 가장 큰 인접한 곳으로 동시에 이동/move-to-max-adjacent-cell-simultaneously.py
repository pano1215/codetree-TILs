import sys

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r_c = [list(map(int, input().split())) for _ in range(m)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

max_num = -sys.maxsize

visited_arr = []

def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def Check(r, c) :
    global max_x, max_y, max_num
    for dx, dy in zip(dxs, dys) :
        next_x, next_y = r + dx, c + dy

        if is_in_range(next_x, next_y) and max_num <= arr[next_x][next_y] :
            max_num = arr[next_x][next_y]
            max_x = next_x
            max_y = next_y
    return max_x, max_y

for _ in range(t) :
    for i in range(m) :
        r = r_c[i][0]
        c = r_c[i][1]

        max_x, max_y = Check(r, c)
        if [max_x, max_y] not in visited_arr: # 처음 등장한 원소
            visited_arr.append([max_x, max_y])
        else:
            continue
            
# print(max_x, max_y)
# print(visited_arr)
print(len(visited_arr))