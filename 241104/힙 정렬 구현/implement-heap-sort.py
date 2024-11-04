# 힙 정렬 함수
def heap_sort(arr):
    n = len(arr)

    # 배열을 최대 힙으로 변환
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 최대 힙에서 요소를 하나씩 꺼내 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 현재 루트(최대값)를 끝으로 이동
        heapify(arr, i, 0)  # 힙 크기를 줄이고 루트를 재정렬

# 힙을 유지하는 함수
def heapify(arr, n, i):
    largest = i       # 루트를 가장 큰 값으로 가정
    left = 2 * i + 1  # 왼쪽 자식 노드
    right = 2 * i + 2 # 오른쪽 자식 노드

    # 왼쪽 자식이 루트보다 크다면 largest를 왼쪽 자식으로 갱신
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 largest보다 크다면 largest를 오른쪽 자식으로 갱신
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 루트가 아니라면, 위치를 교환하고 힙을 재정렬
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# 사용자로부터 n개의 원소를 입력받아 정렬하는 프로그램
n = int(input())
arr =  list(map(int, input().split()))

# 힙 정렬 수행
heap_sort(arr)

# 정렬된 결과 출력
for num in arr :
    print(num, end = ' ')