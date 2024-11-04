cmd = list(input())
stack = []

for parentheses in cmd :
    if len(stack) == 0 :
        stack.append(parentheses)
    else : 
        if parentheses == ')' :
            if stack[-1] == '(' :
                stack.pop()
        else : # (인 경우
            stack.append(parentheses)

if len(stack) == 0 :
    print('Yes')
else : 
    print('No')