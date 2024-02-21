t = int(input())

test_cases = []
for _ in range(t):
    n, m = map(int, input().split())

    for _ in range(m) :
        x, y, d = input().split()
        test_cases.append([x, y, d])   

print(test_cases)