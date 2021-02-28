from collections import deque
def BSF(x,y):

    start_point = (x,y)
    queue = deque()
    queue.append(start_point)

    while queue:
        now=queue.popleft()
        for i in range(4): # 각 방향마다 하나씩 더해줘서 for문으로 4방향을 모두 다뤄보고 if문으로 나머지 제거 하는 거지.
            search[0]=now[0]+dx[i]
            search[1]=now[1] + dy[i]
            if search[0]>n-1 or search[1]>m-1 or search[0]<0 or search[1]<0: # 이 조건 빠뜨렸네...
                continue # 여기서 continue로 빠지는 건 더이상 이 지점은 의미가 없으니 4방향 중 다른 지점을 보라는 의미
            if graph[search[0]][search[1]] == 0: # 인덱싱을 한 대괄호에 하는 게 어딧냐,, ㅄ아
                continue
            if graph[search[0]][search[1]] == 1:
                graph[search[0]][search[1]] =graph[now[0]][now[1]]+1
                queue.append(search) # append는 하나만 더해야지
    return graph[n-1][m-1] # while문이 끝나고 리턴읋 해야지.

n, m = list(map(int, input().split()))

graph = []
search = [0,0]
for i in  range(n):
    graph.append(list(map(int, input()))) #그래프의 성분을 인트로 받기위해서 저렇게 매핑을 한거임.


dx = (0, 0, 1, -1) #tuple은 그냥 변하지 않는 것만 이렇게 설정해 주면 되는 거고. 리스트랑 똑같네
dy = (1, -1, 0, 0)

print(BSF(0,0))





