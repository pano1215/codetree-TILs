n = int(input())
car_price = list(map(int, input().split()))

# 오른쪽에서부터 최대값을 기록하는 배열을 생성합니다.
max_future_price = [0] * n
max_future_price[-1] = car_price[-1]

# 역순으로 최대값을 저장합니다.
for i in range(n - 2, -1, -1):
    max_future_price[i] = max(car_price[i], max_future_price[i + 1])

max_price = 0 
for i in range(n) :
    max_price = max(max_price, max_future_price[i] - car_price[i])

print(max_price)