n, k = map(int, input().split())
ans = []

def Print() :
    for e in ans :
        print(e, end = ' ')
    print()

def review(num) :
    if num == k + 1 :
        Print()
        return

    for i in range(1, n + 1) :
        ans.append(i)
        review(num + 1)
        ans.pop()

review(1)