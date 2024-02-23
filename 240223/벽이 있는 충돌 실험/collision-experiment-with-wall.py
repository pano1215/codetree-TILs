t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 격자 안에 있는 범위 탐색
def is_in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

# 남은 구슬들 세기
def count(test_cases) :
    global cnt 

    for i in range(len(test_cases)) :
        x = test_cases[i][0]
        y = test_cases[i][1]

        if x != n and y != n :
            cnt += 1
    return cnt

# 겹치는 요소들 삭제하기
def remove(visited, test_cases, row, col) :
    for i in range(len(test_cases)) :
        # test_cases에서 row와 col이 같은 것을 n으로 설정 
        x = test_cases[i][0]
        y = test_cases[i][1]

        if row == x and col == y :
            test_cases[i][0] = n
            test_cases[i][1] = n
    return test_cases

# 격자에서 벗어나는 경우 - 방향을 전환하는 함수
def change_dirt(d) :
    d = (d + 2) % 4
    return d 

# 이동하는 함수
def move(i, x, y, d) :
    next_x = x + dx[d]
    next_y = y + dy[d]
    if is_in_range(next_x, next_y) :
        test_cases[i][0] = next_x
        test_cases[i][1] = next_y
        test_cases[i][2] = d

        return next_x, next_y, d
    else : 
        d = change_dirt(d) 

        test_cases[i][0] = x
        test_cases[i][1] = y
        test_cases[i][2] = d

        return x, y, d
    
for _ in range(t):
    test_cases = []
    n, m = map(int, input().split())

    for _ in range(m) :
        x, y, d = input().split()

        if d == 'R' :
            d = 0
        elif d == 'D' :
            d = 1
        elif d == 'L' :
            d = 2
        elif d == 'U' :
            d = 3

        x = int(x) - 1
        y = int(y) - 1
        test_cases.append([x, y, d])   

    for _ in range(n * 2) : # 격자의 *2만큼 반복하면 무한히 반복되는게 확정되려나  
        visited = [[0 for _ in range(n)] for _ in range(n)] # 방문한 구슬 숫자 기록하기
        for i in range(m) : # 구슬들의 조건을 반복함
            x = test_cases[i][0]
            y = test_cases[i][1]
            d = test_cases[i][2]
            
            if x >= n or y >= n :# x 또는 y가 n을 넘어가면 깨진 구슬이라는 의미이므로 패스
                continue 

            x, y, d = move(i, x, y, d)
            visited[x][y] += 1

        for row in range(len(visited)) :
            for col in range(len(visited[0])) :
                if visited[row][col] >= 2 : 
                    test_cases = remove(visited, test_cases, row, col)
    cnt = 0
    result = count(test_cases)
    
    print(result)