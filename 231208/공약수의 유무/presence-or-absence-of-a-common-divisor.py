a, b = map(int, input().split())
found = 0
num = 1
while num <= 2880 :
    if 1920 % num == 0 and 2880 % num == 0:
        if a <= num <= b :
            found = 1
            break 
    num += 1
if found == 1 :
    print(1)
else : 
    print(0)

# if 1920 % num == 0 and 2880 % num == 0:
#     if not(a <= num <= b) :
#         print(0)