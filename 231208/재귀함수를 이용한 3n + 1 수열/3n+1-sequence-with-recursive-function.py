import sys
sys.setrecursionlimit(10**7)

n = int(input())
cnt = 0

def coutn(n, cnt) :
    if n == 1 :
        return cnt

    if n % 2 == 0 :
        n /= 2
        cnt += 1
        return coutn(n, cnt)
    else : 
        n = (n * 3) + 1
        cnt += 1
        return coutn(n, cnt)

print(coutn(n, cnt))