# 입력
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 선언
r -= 1
c -= 1

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

delete_num = arr[r][c] 
arr[r][c] = 0

# 격자 범위 체크
def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 네 방향을 탐색하며 0으로 바꿔주는 함수
def Change_zero(r, c) :
    for dx, dy in zip(dxs, dys) :
        for step in range(delete_num - 1) :
            next_x = r + dx
            next_y = c + dy

            if is_in_range(next_x, next_y) :
                arr[next_x][next_y] = 0

                r = next_x
                c = next_y
    return arr

print(Change_zero(r, c))