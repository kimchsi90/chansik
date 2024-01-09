S = list(map(int, input()))

result = int(S[0])
list_sum = [0, 1]

for i in range(1, len(S)):
    if result in list_sum or S[i] in list_sum:
        result += S[i]
    else:
        result *= S[i]

print(result)
