n,m,k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
largest = data.pop()
second = data.pop()

result_list = [largest]*m # 여기 다시 보기

num_second = m//k

for i in range(1,num_second+1):
    result_list[(k+1)*i-1]=second

result=sum(result_list)
print(result)
