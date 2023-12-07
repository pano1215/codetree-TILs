n = int(input())

for i in range(n, 0, -1):
    for j in range(n, 0, -1) :
        if i < j :
            print(' ', end = ' ')
        else :
            print(j, end = ' ')
    print()

# for i in range(n) :
#     #print(' ' * i)
#     for j in reversed(range(n - i)) :
#         if i < j :
#             print(' ')
#         else : 
#             print(j+1, end = ' ')
#     print()