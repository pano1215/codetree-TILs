first_age, first_gender = map(str, input().split())
second_age, second_gender = map(str, input().split())

if (int(first_age) >= 19 and first_gender == 'M') or (int(second_age) >= 19 and second_gender == 'M') :
    print(1)
else :
    print(0)