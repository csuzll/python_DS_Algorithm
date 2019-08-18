from Graph import Graph
from Queue import Queue
from Vertex import Vertex

# 此方法创建word图(无向图，边无权)
def buildGraph(wordFile):
    """
        wordFile为word文件名
    """
    d = {}
    g = Graph()

    # create buckets of words that differ by one letter
    with open(wordFile, "r") as f:
        lines = f.readlines()

    # 使用桶存储word。每一个桶中的word都是能够形成一条边的任意两个顶点
    for line in lines:
        # word = line[:-1]
        word = line.strip() # 删除换行符
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:] # 桶关键字
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # 在相同的桶内添加顶点和边（权重为0）
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    return g

# bfs算法构建了每个顶点到起始顶点的最短距离
def bfs(g, start):
    """
        g: 待搜索的图
        start: 搜索的起始顶点
    """
    start.setColor("gray") # 起始顶点设置为灰色，表明正在被探索
    start.setDistance(0) # 到起始顶点的距离设置为0
    start.setPredecessor(None) # 起始顶点的前导顶点设置为None
    vertQueue = Queue() # 顶点队列
    vertQueue.enqueue(start) # 将起始顶点放入顶点队列中

    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue() # 当前顶点为弹出的队首顶点
        for nbr in currentVert.getConnections(): # 当前顶点的所有邻接顶点
            # 新的顶点，未被访问过
            if nbr.getColor() == "white":
                nbr.setColor("gray") # 1、颜色设置为灰色
                nbr.setDistance(currentVert.getDistance() + 1) # 2、到nbr的距离设置为到currentVert的距离 + 1
                nbr.setPredecessor(currentVert) # 3、nbr的前导顶点设置为currentVert
                vertQueue.enqueue(nbr) # 4、nbr添加到队列末尾
        currentVert.setColor("black") # 当前结点的邻接结点都添加到队列中后，设置当前顶点的颜色为黑色

# 打印从某个顶点到起始顶点的最短路径
def traverse(vert):
    x = vert
    # 此顶点非起始顶点
    while x.getPredecessor():
        print(x.getId()) 
        x = x.getPredecessor()
    # 此顶点为起始顶点
    print(x.getId())

if __name__ == "__main__":
    g = buildGraph("fourletterwords.txt") # 要搜索的图
    start = g.getVertex("FOOL") # 起始顶点
    bfs(g, start)
    end = g.getVertex("SAGE")
    traverse(end)




