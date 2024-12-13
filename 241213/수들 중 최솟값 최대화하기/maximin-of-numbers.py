import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
pick = [] 

min_val = sys.maxsize
max_val = -sys.maxsize 

def start(row) :
    global min_val, max_val

    if row == n :
        sum_val = 0
        for num in pick :
            sum_val += num
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

    max_val = max(min_val, max_val)

start(0)
print(max_val)