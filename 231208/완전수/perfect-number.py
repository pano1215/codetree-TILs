start, end = map(int, input().split())

cnt = 0
for i in range(start, end + 1) :
    im_sum = 0
    for j in range(1, i):
        if i % j == 0 :
            im_sum += j
    if im_sum == i :
        cnt += 1
print(cnt)