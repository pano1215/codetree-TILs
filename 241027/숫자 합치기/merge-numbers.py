import heapq

n = int(input())
num = list(map(int, input().split()))

heapq.heapify(num)

cost = 0
while len(num) > 1 :
    min1 = heapq.heappop(num)
    min2 = heapq.heappop(num)
    
    temp_cost = min1 + min2
    cost += temp_cost

    heapq.heappush(num, temp_cost)

print(cost)