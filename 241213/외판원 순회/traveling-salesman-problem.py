import sys

# 입력값 받기
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
pick = []

min_val = sys.maxsize

def start(row) :
    global min_val 

    if len(pick) == n :
        sum_val = 0
        for num in pick :
            if arr[num][pick[num]] == 0 :
                return 
            sum_val += arr[num][pick[num]]
        min_val = min(min_val, sum_val)
        return min_val

    for i in range(n) :
        if visited[i] :
            continue
        
        visited[i] = True
        pick.append(i)

        start(row + 1)

        visited[i] = False
        pick.pop()
        

start(0)

print(min_val)