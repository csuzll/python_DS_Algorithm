G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

#Breadth first search
def bfs(G,start):
    seen = [start]
    q = [start]  #先进先出的队列
    while q:
        cur = q.pop(0)
        for vertex in G[cur]:
            if vertex not in seen:
                seen.append(vertex)
                q.append(vertex)
    return seen
print(bfs(G,'C'))