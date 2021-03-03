import itertools

n = int(input())
data = list(map(int,input().split()))
total_candi =[]
combi_list = [0]*n
for i in range(1,n+1):
    combi_list[i-1] = list(itertools.combinations(data, i))

for j in range(0, len(combi_list)):
    for k in range(0, len(combi_list[j])):
        candi=sum(combi_list[j][k])
        total_candi.append(candi)

minimum = 1
while 1:
    if minimum in total_candi:
        minimum +=1
        continue
    else:
        break
print(minimum)

