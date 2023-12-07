# 변수 선언 및 입력
n = int(input())
cnt = 0
	
# 값을 조건대로 증가시켜 출력합니다.
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            cnt += 1
        else:
            cnt += 2
        print(cnt, end=" ")
    print()

# n = int(input())

# cnt = 0
# for i in range(n):
#     if i % 2 == 0 :
#         for j in range(n):
#             # if j == 0 :
#             #     cnt += 1
#             print(cnt, end = ' ')
#             cnt += 1 
#         # cnt += 1
#     else :
#         for j in range(n):  
#             # if j == 0 :
#             #     cnt += 1
#             print(cnt, end = ' ') 
#             cnt += 2   
#         # cnt -= 1
#     print()
     
#   0  1  2  3 
# 0 1  2  3  4
# 1 6  8  10 12
# 2 13 14 15 16
# 3 18 20 22 24

# i * 2