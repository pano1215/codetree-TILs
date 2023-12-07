n = int(input())
cnt = 0

def count(n, cnt) :
    if n == 1 :
        return cnt 

    if n % 2 == 0 :
        cnt += 1
        return count(n // 2, cnt)
    else :
        cnt += 1
        return count(n // 3, cnt)

print(count(n, cnt))