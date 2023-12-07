n = int(input())

for i in range(n, 0, -1) :
    for j in range(i):
        print("*", end='')
    for j in range(n - i):
        print(' ', end='')
    for j in range(n - i):
        print(' ', end='')
    for j in range(i):
        print("*", end='')
    print()


# 첫 줄 : n * 2
# 두번째 줄 : n-1 스페이스 n-1
# 세번째 줄 : n-2 스페이스 n-2
# 네번째 줄 : n-3 스페이스 n-3