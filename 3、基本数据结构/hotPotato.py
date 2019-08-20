from queue import Queue

# 模拟Hot Potato游戏
# 类似于击鼓传花，约瑟夫环问题（n个人围成一圈，从1开始报数，每当有人报到m时，他被淘汰，下一个人继续从1开始报数，问最后的获胜者是谁？）

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

if __name__ == '__main__':
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
    print("\n")
    # 随机的时间比较长
    print(hotPatato2(["Bill","David","Susan","Jane","Kent","Brad"]))