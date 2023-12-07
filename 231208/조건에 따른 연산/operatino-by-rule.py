a = int(input())

cnt = 0
while a <= 1000 :
    if a % 2 == 0 :
        a = (a * 3) + 1
    else :
        a = (a * 2) + 2
    cnt += 1
print(cnt)