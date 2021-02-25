array = list(map(int, input().split()))
N_array = len(array)

sum = 0
product = 0
result = array[0]
for i in range(N_array-1):
        sum = result + array[i+1]
        product = result * array[i+1]
        if sum > product:
            result = sum
        else:
            result = product

print(result)