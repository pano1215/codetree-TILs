n, m, k = map(int, input().split())
turn = list(map(int, input().split()))
pieces = [1 for _ in range(k)]

ans = 0 

def cal() :
    score = 0 

    for p in pieces :
        score += (p >= m)
    
    return score

def find_max(cnt) :
    global ans

    ans = max(ans, cal())

    if cnt == n :
        return 

    for i in range(k) :
        if pieces[i] >= m :
            continue
        
        pieces[i] += turn[cnt]
        find_max(cnt + 1)
        pieces[i] -= turn[cnt]

find_max(0)
print(ans)