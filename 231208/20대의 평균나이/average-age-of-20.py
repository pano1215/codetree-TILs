age_sum, cnt = 0, 0

while True :
    try:
        age = int(input())

        if age >= 20 and age <= 29 :
            age_sum += age
            cnt += 1
    except EOFError:
        break
print(f"{round(age_sum / cnt, 2):.2f}")