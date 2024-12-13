import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
pick = [] 

max_val = -sys.maxsize 

def start(row) :
    global min_val, max_val

    if row == n :
        min_val = sys.maxsize
        for num in range(len(pick)) :
            #sum_val += arr[num][pick[num]]
            
            min_val = min(min_val, arr[num][pick[num]])
            #print('arr[num][pick[num]] : ', arr[num][pick[num]], min_val)
        #print('갱신 끝')
        return min_val

    for i in range(n) :
        if visited[i] :
            continue
        
        visited[i] = True
        pick.append(i)
        #print('pick : ', pick)
        #print('visited : ', visited)
        start(row + 1)

        visited[i] = False
        pick.pop()

        max_val = max(min_val, max_val)

start(0)
print(max_val)