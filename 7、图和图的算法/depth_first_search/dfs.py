# 实现一个简单的dfs

# G为图G
G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

# 简单的遍历
def dfs(G, start):
    seen = [start]   # 已发现的结点列表
    stack = [start]  # 先进后出的栈
    path = [] # dfs遍历结果
    while stack:
        cur = stack.pop()
        path.append(cur)
        for vertex in G[cur]:
            if vertex not in seen:
                seen.append(vertex)
                stack.append(vertex)
    return path

print(dfs(G,"A"))