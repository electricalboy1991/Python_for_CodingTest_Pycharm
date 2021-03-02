n,m = map(int,input().split())
data = [[0]*m for _ in range(n)]

for i in range(n):
    data[i][:] = list(map(int, input().split())) # 인덱싱을 자꾸 실수하네.

min_list = [0]*n

for k in range(n):
    temp_min = min(data[k][:]) # min안에 리스트 넣어도 min값 찾아주네.
    min_list[k] = temp_min

min_list.sort()

print(min_list[-1])
