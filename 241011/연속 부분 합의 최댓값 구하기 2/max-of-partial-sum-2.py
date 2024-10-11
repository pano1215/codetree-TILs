n = int(input())
num = list(map(int, input().split()))

max_arr = []
max_arr.append(max(num))

ans = 0 
for i in range(n) :
    ans += num[i]
    if ans < 0 :
        ans = 0
    max_arr.append(ans)

if all(x < 0 for x in num) :
    print(max(num))
else :
    print(max(max_arr))