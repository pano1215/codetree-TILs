from collections import deque

n = int(input())
arr = list(map(int, input().split()))

def find_min(n, arr) :
    visited = [False] * n 
    jump_cnt = 0
    q = deque([(0, 0)])

    visited[0] = True

    while q :
        postion, jump_cnt = q.popleft()

        for i in range(postion + 1, postion + arr[postion] + 1) :
            if i == n - 1 :
                return jump_cnt + 1

            visited[i] = True
            q.append((i, jump_cnt + 1))

print(find_min(n, arr))