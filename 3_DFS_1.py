def dsf(j,k):
    if j<0 or k<0 or j>n-1 or k>m-1:
        return False # False를 return했다는 거는 더이상 볼 필요가 없다는 의미임

    if graph[j][k]==0:
        graph[j][k]=1
        dsf(j - 1, k)
        dsf(j, k - 1)
        dsf(j + 1, k)
        dsf(j, k + 1)
        return True
    return False # False를 리턴했다는 거는 더이상 볼 필요가 없다는 의미임.

n, m = list(map(int, input().split()))

graph = []
result = 0

for i in  range(n):
    graph.append(list(map(int, input()))) #그래프의 성분을 인트로 받기위해서 저렇게 매핑을 한거임.

for j in range(n):
    for k in range (m):
        if dsf(j,k) == True: #인접한 모든 지점에 graph에 1을 찍고나서 그 때 result에 1을 더하겠다는 의미지.
            result+=1

print(result)

