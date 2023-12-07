a, b = map(int, input().split())
i = 1
for num in range(1, b + 1) :
    if num % a == 0 :
        i = i * num
print(i)