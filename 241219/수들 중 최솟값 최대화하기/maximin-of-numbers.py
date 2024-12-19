# 최솟값이 최대 

import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

pick = []
visited = [False] * n 
min_arr = []

def find_min(pick) :
    global min_val, min_arr

    min_val = sys.maxsize
    for i in pick :
        min_val = min (min_val, arr[i][pick[i]])
    
    min_arr.append(min_val)
     
def find_max(row) :
    if len(pick) == n : 
        #print(pick)
        find_min(pick)
        return 

    for i in range(n) :
        if visited[i] : 
            continue

        visited[i] = True
        pick.append(i)

        find_max(row + 1)

        visited[i] = False
        pick.pop()

find_max(0)

print(max(min_arr))