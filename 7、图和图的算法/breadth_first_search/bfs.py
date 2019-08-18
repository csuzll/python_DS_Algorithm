# 实现一个简单的bfs

# G为图G
G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

#Breadth first search
def bfs(G, start):
    seen = [start] # 按顺序已访问的顶点列表
    q = [start]  # 先进先出的队列
    while q:
        cur = q.pop(0)
        for vertex in G[cur]:
            if vertex not in seen:
                seen.append(vertex)
                q.append(vertex)
    return seen

print(bfs(G,'C'))