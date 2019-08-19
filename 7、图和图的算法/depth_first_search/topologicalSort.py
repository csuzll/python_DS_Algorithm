# 拓扑排序
from DFSGraph import DFSGraph
from Vertex import Vertex

def topologicalSort(g):
    """以完成时间的递减顺序将顶点存储在列表中，这个列表就是拓扑排序的结果"""
    g.dfs()
    result = list(g)
    result.sort(key=lambda x : x.finish, reverse=True)
    for vert in result:
        print(vert.getId())
    
# vertsName = ["3/4_cup_milk", "1_cup_mix", "1_egg", "1_Tbl_Oil", "heat_syrup", "heat_griddle", "pour_1/4_cup", "turn_when_bubbly", "eat"]

g = DFSGraph()
g.addEdge("3/4_cup_milk", "1_cup_mix")
g.addEdge("1_egg", "1_cup_mix")
g.addEdge("1_Tbl_Oil", "1_cup_mix")
g.addEdge("1_cup_mix", "pour_1/4_cup")
g.addEdge("1_cup_mix", "heat_syrup")
g.addEdge("heat_syrup", "eat")
g.addEdge("heat_griddle", "pour_1/4_cup")
g.addEdge("pour_1/4_cup", "turn_when_bubbly")
g.addEdge("turn_when_bubbly", "eat")

topologicalSort(g)
