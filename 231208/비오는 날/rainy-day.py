# 변수 선언 및 입력
n = int(input())


# Forecast 정보를 나타내는 클래스 선언
class Forecast:
    def __init__(self, date, day, weather):
        self.date, self.day, self.weather = date, day, weather


ans = Forecast("9999-99-99", "", "")
for _ in range(n):
    date, day, weather = tuple(input().split())

    # Forecast 객체를 만들어 줍니다.
    f = Forecast(date, day, weather)
    if weather == "Rain":
        # 비가 오는 경우 가장 최근인지 확인하고,
        # 가장 최근일 경우 정답을 업데이트합니다.
        if ans.date >= f.date:
            ans = f

# 결과를 출력합니다.
print(ans.date, ans.day, ans.weather)