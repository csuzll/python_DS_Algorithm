from queue import Queue

# 模拟Hot Potato游戏
# 类似于击鼓传花，约瑟夫环问题。

def hotPotato(namelist, num):

    # namelist: 姓名队列
    # num: 出队入队num次
    simqueue = Queue()

    # 将姓名list转为列表表示
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        # 在出入队列num次后，将队首的元素删除
        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))


# 修改hotPotato算法，使每次传递的个数为一个随机数。
import random

def hotPatato2(namelist):

    simqueue = Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        num = random.randrange(1, 5)
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue)
        simqueue.dequeue()
    return simqueue.dequeue()

print(hotPatato2(["Bill","David","Susan","Jane","Kent","Brad"]))