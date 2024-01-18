n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

cur_x, cur_y = r - 1, c - 1
compare_num = arr[cur_x][cur_y]
visited_arr = [] 
visited_arr.append(compare_num)

def is_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < n

def move() :
    for dx, dy in zip(dxs, dys) :
        global next_x, next_y, cur_x, cur_y, compare_num
        next_x, next_y = cur_x + dx, cur_y + dy
        #print(dx, dy)
        #print(next_x, next_y)
        if is_range(next_x, next_y) and arr[next_x][next_y] > compare_num :
            #print(next_x, next_y)
            # visited_arr.append(arr[next_x][next_y])
            compare_num = arr[next_x][next_y]

            cur_x = next_x
            cur_y = next_y

            return True 
       
    return False

while True :

    if not move() :
        break

    visited_arr.append(arr[next_x][next_y])

for e in visited_arr :
    print(e, end = ' ')