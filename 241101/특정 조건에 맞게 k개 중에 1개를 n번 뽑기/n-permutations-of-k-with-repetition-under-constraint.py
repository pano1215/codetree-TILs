k, n = map(int, input().split())
ans = []

def select_num() : 
    if len(ans) == n :
        for i in range(len(ans)) :
            print(ans[i], end = ' ')
        print()
        return 

    for num in range(1, k + 1) :
        if len(ans) >= 2 and ans[-1] == ans[-2] == num :
            continue
    
        ans.append(num)
        select_num()
        ans.pop()

select_num()