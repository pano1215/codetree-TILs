n = int(input())

i, cnt = 1, 0
while n >= 1 :
    n = n // i
    cnt += 1
    i += 1
    
    if n <= 1 :
        break
print(cnt)