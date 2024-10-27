from functools import cmp_to_key

n = int(input())
num = [str(input()) for _ in range(n)]

def compare(x, y) :
    if x + y > y + x :
        return -1
    if x + y < y + x :
        return 1
    if x + y == y + x :
        return 0

def make(num) :
    num.sort(key = cmp_to_key(compare))
    result = ''.join(num)
    print(result)

make(num)