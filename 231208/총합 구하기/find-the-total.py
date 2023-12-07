a, b = map(int, input().split())
i = 0
for num in range(a, b + 1) :
    if num % 6 == 0 and num % 8 != 0 :
        i = i + num
print(i)