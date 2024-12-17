from collections import deque

n = int(input())
arr = list(map(int, input().split()))

def start(n, arr) :
    visited = [False] * n
    q = deque([(0, 0)])

    visited[0] = True

    while q :
        curr, jump_cnt = q.popleft()

        for i in range(curr + 1, curr + 1 + arr[curr]) : 
            if i == n - 1 :
                return jump_cnt + 1
            
            visited[i] = True
            q.append((i, jump_cnt + 1))
    return -1 

print(start(n, arr))