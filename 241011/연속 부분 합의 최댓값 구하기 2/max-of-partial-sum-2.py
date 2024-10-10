n = int(input())
num = list(map(int, input().split()))

ans = 0 
if all(n < 0 for n in num) :
    ans = max(num)
else :
    for i in range(n) : 
        ans += num[i]
        if ans < 0 :
            ans = 0
print(ans)