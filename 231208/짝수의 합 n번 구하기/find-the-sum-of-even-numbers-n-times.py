n = int(input())

for i in range(n) :
    a, b = map(int, input().split())
    sum = 0
    for j in range(a, b+1): # a부터 b까지 숫자를 뽑음
        if j % 2 == 0 : # 짝수인 경우
            sum += j # 짝수인 경우 합을 구함
    print(sum)