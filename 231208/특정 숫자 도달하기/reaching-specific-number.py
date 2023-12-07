arr = list(map(int, input().split()))

sum = 0
avg = 0
cnt = 0 
for i in arr :
    if i <= 250 :
        sum += i
        cnt += 1
    if i >= 250 :
        break

avg = sum / cnt
print(sum, "{:.1f}".format(avg))