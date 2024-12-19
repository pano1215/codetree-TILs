import sys

max_val = -sys.maxsize

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
pick = []

def make_sum(row) :
    global max_val

    if len(pick) == n :
        #print(pick)
        sum_val = 0 
        for num in pick :
            sum_val += arr[num][pick[num]]

        max_val = max(max_val, sum_val)
        return 

    for i in range(n) :
        if visited[i] :
            continue

        visited[i] = True
        pick.append(i)

        make_sum(row + 1)

        visited[i] = False
        pick.pop()

make_sum(0)

print(max_val)