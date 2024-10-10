n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin = coin[::-1]

result = 0 
for i in coin :
    result += k // i
    k %= i
print(result)