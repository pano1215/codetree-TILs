n = int(input())
car_price = list(map(int, input().split()))

price_diff = [0] * n
price_diff[-1] = car_price[-1]
for i in range(n - 2, -1, -1) :
    if len(price_diff) == 0 :
        price_diff[i] = car_price[i]
    else : 
        if price_diff[i + 1] >= car_price[i] :
            price_diff[i] = price_diff[i + 1]
        else :
            price_diff[i] = car_price[i]
#print(price_diff)

diff = []
for i in range(n) :
    diff_price = price_diff[i] - car_price[i]
    diff.append(diff_price)

print(max(diff))