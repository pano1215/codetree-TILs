n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# m이상으로 연속하는 폭탄이 있는지 체크
def Same_check(start_idx, curr_num) :
    for i in range(start_idx + 1, len(arr)) :
        if arr[i] != curr_num  :
            return i - 1
    return len(arr) - 1

while True :
    same_check = False
    cur_idx = 0

    while cur_idx < len(arr) :
        end_idx = Same_check(cur_idx, arr[cur_idx]) 

        if end_idx - cur_idx + 1 >= m :
            del arr[cur_idx : end_idx + 1]
            same_check = True
        else :
            cur_idx = end_idx + 1

    if not same_check :
        break

# 정답 출력
print(len(arr))

for ca in arr :
    print(ca)