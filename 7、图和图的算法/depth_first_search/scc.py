# 求图的强连通分量

# 邻接集表示图
G = {
    "a": {"b"},   #a
    "b": {"c"},   #b
    "c": {"a","d","g"},   #c
    "d": {"e"},   #d
    "e": {"f"},   #e
    "f": {"d"},   #f
    "g": {"h"},   #g
    "h": {"i"},   #h
    "i": {"g"}    #i
}

# 图的翻转
def transgraph(g):
    gt = {}
    for u in g:
        for v in g[u]:
            if gt.get(v):
                gt[v].add(u)
            else:
                gt[v] = set()
                gt[v].add(u)
    return gt

# 图的DFS
def rec_dfs(g, s, S=None):
    """
    g: 图
    s: 起始结点
    S: 按顺序发现的结点集，初始时为None
    """
    if S is None:
        S = list() # 存储已遍历的结点
    S.append(s)
    # print(S)
    for u in g[s]:
        if u in S:
            continue
        rec_dfs(G, u, S)
    return S

# 遍历有向图的强连通图(只能得到一个从参数start出发的连通分量)
def walk(g, start, S=set()):
    P, Q = dict(), set() # P存放，Q存放已经遍历的结点
    P[start] = None # 起始结点的前一个结点为None
    Q.add(start)
    while Q:
        u = Q.pop() # 选择下一个遍历结点（集合具有随机性）
        for v in g[u].difference(P, S): # u的邻接结点中没有出现在P和S中的结点
            Q.add(v) 
            P[v] = u
    # print(P)
    return P

# 获得各个强连通分量
def scc(g):
    gt = transgraph(g)

    sccs = [] # 强连通分量列表
    seen = set() # 已遍历结点集合

    for u in rec_dfs(g, "a"): # 以"a"为起点
        if u in seen:
            continue
        C = walk(gt, u, seen)
        seen.update(C) # 将C中的key添加到seen中
        sccs.append(C) # C为一个强连通分量，加入强连通分量列表中
    return sccs

print(scc(G))