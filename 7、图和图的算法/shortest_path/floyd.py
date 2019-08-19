# floyd算法: 图中任意两点间的最短路径（多源最短路径）
# 算法时间复杂度为O(n^3)

# 下面针对的图为无向加权图

nodes = [1, 2, 3, 4, 5, 6, 7, 8] # 图中的顶点
inf = 999999999 # 无限大的数

# dis保存图的任意两点间的最短距离，初始化为图的权重矩阵
dis = [
        [0, 5, 1, inf, inf, inf, inf, inf],
        [5, 0, 2, 5, inf, inf, inf, inf],
        [1, 2, 0, inf, 1, 3, 2, inf],
        [inf, 5, inf, 0, inf, inf, inf, inf],
        [inf, inf, 1, inf, 0, inf, inf, inf],
        [inf, inf, 3, inf, inf, 0, 6, inf],
        [inf, inf, 2, inf, inf, 6, 0, 1],
        [inf, inf, inf, inf, inf, inf, 1, 0],
]

# 记录最短路径
path = [] 
# path初始化为值全为-1
for i in range(len(nodes)):
    path += [[]]
    for j in range(len(nodes)):
        path[i].append(-1)

# 打印任意两点的最短路径函数
def getPath(path, i, j):
    if i != j:
        if path[i][j] == -1:
            print("-", j+1, end=" ")
        else:
            getPath(path, i, path[i][j])
            getPath(path, path[i][j], j)

def printPath(path, i, j):
    print("Path:", i+1, end=" ")
    getPath(path, i, j)
    print()

# floyd算法
def floyd(vertex, dis):
    """
    vertex: 图中的顶点
    dis: 与图中顶点相对应的初始权重矩阵
    """
    for k in vertex:
        in_k = vertex.index(k)
        for i in vertex:
            in_i = vertex.index(i)
            for j in vertex:
                in_j = vertex.index(j)
                if dis[in_i][in_j] > dis[in_i][in_k] + dis[in_k][in_j]:
                    dis[in_i][in_j] = dis[in_i][in_k] + dis[in_k][in_j]
                    path[in_i][in_j] = in_k

floyd(nodes, dis)


# 打印结果
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        print('v%d <----> v%d tol_weight:''%3d' % (i+1, j+1, dis[i][j]), '', end='')
        printPath(path, i, j)