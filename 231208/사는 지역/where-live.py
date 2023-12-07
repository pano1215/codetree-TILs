class Address:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region
        
        
# 변수 선언 및 입력
n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [Address(name, address, region) for name, address, region in arr]

# 사전순으로 이름이 가장 느린 사람 찾기
target_idx = 0
for i, person in enumerate(people):
    if person.name > people[target_idx].name:
        target_idx = i

# 결과 출력
print(f"name {people[target_idx].name}")
print(f"addr {people[target_idx].address}")
print(f"city {people[target_idx].region}")