n = int(input())
arr = list(map(int, input().split()))

def f(a, b) :
    if b == 0 :
        return a
    return f(b, a % b)

x = arr[0]
y = arr[0]

for i in range(0, n) :
    x = f(y, arr[i])
    y = y * arr[i] // x
print(y)