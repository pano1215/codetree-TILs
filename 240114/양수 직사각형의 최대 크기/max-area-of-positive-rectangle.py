n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def is_range(x, y) :
    return 0 <= x and x < n and 0 <= y and y < m 

def check(row, col, wid, hei) :
    for i in range(row, row + hei) :
        for j in range(col, col + wid) :
            if not is_range(i, j) :
                return False
            if arr[i][j] < 0 :
                return False
    return True

def count(row, col, wid, hei) :
    cnt = 0
    for i in range(row, row + hei) :
        for j in range(col, col + wid) :
            cnt += 1
    return cnt

result = -1 
for row in range(n) :
    for col in range(m) :
        for wid in range(1, n + 1) :
            for hei in range(1, m + 1) :
                if check(row, col, wid, hei) :
                    result = max(result, count(row, col, wid, hei))

print(result)