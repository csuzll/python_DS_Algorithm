# depth first search    
def dfs(G, start):
    seen = [start]
    stack = [start]    #先进后出的栈
    path = []
    while stack:
        cur = stack.pop()
        path.append(cur)
        for vertex in G[cur]:
            if vertex not in seen:
                seen.append(vertex)
                stack.append(vertex)
    return path
print(dfs(G,"C"))