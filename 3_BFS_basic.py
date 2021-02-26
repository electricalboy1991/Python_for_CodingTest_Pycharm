from collections import deque #bsf는 넓이 탐색으로 얕은거 순서대로 제거하면서 갈 거라서 deque 사용

def bsf(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue: #queue에 원소가 있을 때 까지 while문 돌려라는 의미 다 빠져서 print다 해버리면 종료하는 거지
        v = queue.popleft()
        print(v, end=' ') # 뽑힌 순서대로 내가 방문한 순서라는 개념에서 print를 여기다가 넣는 거야
        for i in graph[v]:
            if not visited[i]:
                queue.append(i) #방문을 안한 것들에 대해서, queue에 다 넣어주고
                visited[i]=True # 다 넣었으니까 방문처리.


start=1
graph = [[],[2,3,8],[1,7,8],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]# 0번 노드는 없기 때문에 비워 두는 게 인덱싱하기가 편함

visited = [False]*9

bsf(graph,start,visited)
