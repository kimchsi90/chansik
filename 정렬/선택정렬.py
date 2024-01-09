array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

'''
시간 복잡도: O(N**2)
N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함
바깥 for문이 수행될 때마다 N + (N - 1) + (N - 2) + ... + 2 = N(N + 1)/2 - 1 = (N**2 + N - 2)/2 => N**2
상수는 무시하고 가장 차수가 높은 항만 고려하기 때문에

공간 복잡도: O(N)
min_idx 변수 이외에 array의 길이 N만큼의 공간이 필요하기 때문에
'''