def dsf(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        """
                if visited[i] == False:
            dsf(graph,i,visited)
        """
        if not visited[i]:
            dsf(graph,i,visited)


v=1
graph = [[],[2,3,8],[1,7,8],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]# 0번 노드는 없기 때문에 비워 두는 게 인덱싱하기가 편함

visited = [False]*9

dsf(graph,v,visited)
