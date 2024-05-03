import sys

s = int(input())

# n이 과연 어디까지일까 

left = 1                   
right = sys.maxsize
min_num = -1         

while left <= right:                
    mid = (left + right) // 2     
    
    if mid * (mid + 1) // 2 <= s:   
        left = mid + 1  
        min_num = max(min_num, mid)  
    else:
        right = mid - 1     

print(min_num)