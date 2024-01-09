import sys
input = sys.stdin.readline

def main():
    result = 0
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(0, n, k-1): # 0부터 n-1까지 
        partition = arr[i:i+k]
        min_val = min(partition)
        arr[i:i+k] = [min_val] * k
        print(arr)
        if not min_val == partition[-1]:
            result += 1

    return result

print(main())

'''
37 4
31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33

12
'''