n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

pick = [] 
ans = 0  
visited = [False] * n

def find_max(row) : 
    global ans 

    if row == n : 
        #print(pick)
        sum_val = 0
        for i in range(n) : 
            sum_val += arr[i][pick[i]]
        
        ans = max(ans, sum_val)
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

print(ans)