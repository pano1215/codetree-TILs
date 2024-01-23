import sys

arr = list(input())
leng = len(arr)

# i + 1이 초과하는 경우 에러가 나는 것을 방지하기 위해 
def char_in_range(x):
    return 0 <= x < leng

def Count(arr) :  
    cnt = 1  
    result = ''
    for letter in range(leng) :
        if char_in_range(letter + 1) and arr[letter] == arr[letter + 1] :
            cnt += 1
        elif char_in_range(letter + 1) and arr[letter] != arr[letter + 1] :
            result += arr[letter] + str(cnt)
            cnt = 1
        elif letter == leng - 1 :
            result += arr[letter] + str(cnt)
    return result   

def Move(arr) :
    last_temp = arr[-1] 
    for char in range(leng - 1, 0, -1) :
        arr[char] = arr[char - 1]
    arr[0] = last_temp
    result = Count(arr)
    return result

min_leng = sys.maxsize
for i in range(leng) :
    result = Move(arr)
    min_leng = min(min_leng, len(result))

print(min_leng)