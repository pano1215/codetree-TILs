n = int(input())
line_arr = [list(map(int, input().split())) for _ in range(n)]
line = [0] * 1000

# 선분에 x1부터 x2를 체크함
for x1, x2 in line_arr :
    for i in range(x1, x2 + 1) :
        line[i] += 1
print(line)