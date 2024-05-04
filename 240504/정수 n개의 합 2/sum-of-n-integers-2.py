import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0] * n

prefix_sum[0] = arr[0]
for i in range(1, n) :
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

max_sum = -sys.maxsize
for i in range(n - k) :
    sum_sum = prefix_sum[i + k - 1] - prefix_sum[i] + arr[i]
    max_sum = max(max_sum, sum_sum)
print(max_sum)