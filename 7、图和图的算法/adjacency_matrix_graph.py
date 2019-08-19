# 邻接矩阵实现图
import sys

nodes = ["A", "B", "C", "D", "E", "F"] # 图包含的顶点
M = sys.maxsize # 无穷大数, 表示两个顶点间无该方向的连接 # 或者 # M = float("inf")

# 权重矩阵
graph_list = [
    [M, 7, 5, M, M, 1],
    [2, M, M, 7, 3, M],
    [M, 2, M, M, M, 8],
    [1, M, M, M, 2, 4],
    [6, M, M, 5, M, M],
    [M, 1, M, M, 8, M],
]

# 邻接矩阵的边和权重
graph_edges = []
for i in nodes:
    for j in nodes:
        if i!=j and graph_list[nodes.index(i)][nodes.index(j)] != M:
            graph_edges.append((i, j, graph_list[nodes.index(i)][nodes.index(j)]))

"""
# 3元组(from_node, to_node, weight)
print(graph_edges)
[
    ('A', 'B', 7), ('A', 'C', 5), ('A', 'F', 1), 
    ('B', 'A', 2), ('B', 'D', 7), ('B', 'E', 3), 
    ('C', 'B', 2), ('C', 'F', 8), 
    ('D', 'A', 1), ('D', 'E', 2), ('D', 'F', 4), 
    ('E', 'A', 6), ('E', 'D', 5), 
    ('F', 'B', 1), ('F', 'E', 8)
 ]
 """
