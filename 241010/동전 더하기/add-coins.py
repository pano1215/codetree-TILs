n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin = coin[::-1]

i, cnt = 0, 0 
while k > 0 :
    if k >= coin[i] :
        k -= coin[i]
        cnt += 1
    else :
        i += 1
        k -= coin[i]
        cnt += 1
print(cnt)