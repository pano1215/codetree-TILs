from collections import deque

n = int(input())
arr = list(map(int, input().split()))

def min_jump(n, arr) : 
    visited = [False] * n
    q = deque([(0, 0)])

    visited[0] = True

    while q :
        position, jump_count = q.popleft()

        for i in range(position + 1, position + arr[position] + 1) :
            #print('i, arr[i], arr[position], jump_count : ', i, arr[i], arr[position], jump_count)
            #print(position + 1, position + arr[position] + 1)
            if i == n - 1 :
                return jump_count + 1 

            if not visited[i] :
                visited[i] = True
                q.append((i, jump_count + 1))
            
            print(visited, q)
    return -1

print(min_jump(n, arr))