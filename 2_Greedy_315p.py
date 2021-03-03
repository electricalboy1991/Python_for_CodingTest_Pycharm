import itertools

n, m = list(map(int,input().split()))
data = list(map(int,input().split()))

data_set = list(set(data))

dict = {i:data.count(i) for i in data_set} #이거 공부하기

combi_list=list(itertools.combinations(data_set,2)) # combination 쓰는 방법, 메서드랑 함수,

count = 0
for i in range(len(combi_list)):
    count += dict[combi_list[i][0]]*dict[combi_list[i][1]]

print(count)