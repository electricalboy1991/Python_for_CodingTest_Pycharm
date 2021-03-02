n = int(input())
data = list(map(int, input().split()))

num_group = 0
count = 1

for i in range(n):
    if data[i]<= count:
        num_group+=1
        count=1
    else:
        count+=1

print(num_group)
