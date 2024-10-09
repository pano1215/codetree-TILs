n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin = coin[::-1]

ans, i = 0, 0
while k > 0 :
    ans += k // coin[i]
    k %= coin[i]
    i += 1
print(ans)