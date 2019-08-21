# 实现一个简单的bfs，只做简单的遍历

# G为图G
G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

# 利用队列先进先出按顺序弹出
def bfs(G, start):
    seen = [start] # 按顺序已访问的顶点列表
    q = [start]  
    while q:
        cur = q.pop(0)
        for vertex in G[cur]: # 每个结点的邻接结点
            if vertex not in seen:
                seen.append(vertex)
                q.append(vertex)
    return seen

print(bfs(G,'A'))