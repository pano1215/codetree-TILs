n, k = map(int, input().split())
numbers = list(map(int, input().split()))

max_sum = float('-inf')
current_sum = 0
minus_count = 0
left = 0

for right in range(n):
    current_sum += numbers[right]
    if numbers[right] < 0:
        minus_count += 1

    while minus_count > k:
        if numbers[left] < 0:
            minus_count -= 1
        current_sum -= numbers[left]
        left += 1

    max_sum = max(max_sum, current_sum)

print(max_sum)
