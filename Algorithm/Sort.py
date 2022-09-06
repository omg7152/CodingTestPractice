#정렬 : 데이터를 특정한 기준에 따라 순서대로 나열하는것

#1.선택정렬 : 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복 - O(N^2)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
for i in range(len(array)):
    min_idx = i
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j

    array[i], array[min_idx] = array[min_idx], array[i]
print(array)
print()

#2.삽입정렬 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입 - O(N^2) 이지만 정렬정도에 따라 O(N) 까지 달라짐
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)
print()

#3.퀵정렬 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))

#4.계수정렬 : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘 O(N + K)
#           데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
#           동일한 값을 가지는 데이터가 여러개 등장할 때 효과적
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')