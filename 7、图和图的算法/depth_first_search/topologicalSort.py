# 拓扑排序

# 邻接集表示图
G = {
    'a': set('bf'), 
    'b': set('cdf'), 
    'c': set('d'), 
    'd': set('ef'), 
    'e': set('f'), 
    'f': set()
}

def dfs_toposort(g):
    S = set()
    res = [] # 排序结果
    # dfs遍历图
    def dfs(u):
        if u in S:
            return
        S.add(u)
        for v in g[u]:
            if v in S:continue
            dfs(v)
        res.append(u)
    # 检查是否有遗漏的顶点
    for u in g:
        dfs(u)
    # 返回拓扑排序后的顶点列表
    res.reverse()
    return res

print(dfs_toposort(G))