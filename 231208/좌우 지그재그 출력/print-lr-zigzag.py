n = int(input())

# cnt = 1
# for i in range(n):
#     if i % 2 == 0 :
#         for j in range(n):
#             print(cnt, end = ' ')
#             cnt += 1 
#     else :
#         cnt += n-1
#         for j in range(n, 0, -1):  
#             print(cnt, end = ' ') 
#             cnt -= 1 
#         cnt += n + 1
#     print()

# 지그재그 출력
for i in range(n) :
    for j in range(n):
        if i % 2 == 0 :
            print((i * n) + j + 1, end = ' ')
        else : 
            print((i * n) + n - j, end = ' ')
    print()