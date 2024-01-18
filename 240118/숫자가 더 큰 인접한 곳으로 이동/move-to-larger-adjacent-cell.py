n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def is_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < n

def move() :
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    cur_x, cur_y = r - 1, c - 1
    compare_num = arr[cur_x][cur_y]
    visited_arr = [compare_num]

    for dx, dy in zip(dxs, dys) :
        next_x, next_y = cur_x + dx, cur_y + dy
        #print(dx, dy)
        if is_range(next_x, next_y) and arr[next_x][next_y] > compare_num :
            #print('33333')
            visited_arr.append(arr[next_x][next_y])
            compare_num = arr[next_x][next_y]
            cur_x = next_x
            cur_y = next_y
    
    return visited_arr

result = move()

for e in result :
    print(e, end = ' ')