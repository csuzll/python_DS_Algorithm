# -*- coding utf-8 -*-
import random
from queue import Queue

"""
问题描述：
假设实验室里有一台打印机供学生共享。当学生向共享打印机发送打印任务时，任务被放置在队列中以便以先来先服务的方式被处理。
如何才能通过python程序模拟的方式得到每次提交任务的平均等待时间呢？（平均等待时间不包括打印本身的时间，仅指在队列中排队的时间。）
假定：
平均每天大约10名学生在实验室工作，每人每小时打印2次。
学生们每次打印的页数在1到20页之间。
打印机平均每小时会收到20个打印请求，即平均每180秒1个请求。
每秒新增任务的可能性相等，即任务的产生为独立同分布。
打印机的打印速度恒定。
"""

"""
总体模拟思路：
1、创建打印任务的队列，每个任务都有个时间戳。队列启动的时候为空。
2、每秒（second）
    是否创建新的打印任务？如果是，将second作为时间戳添加到队列。
    如果打印机不忙并且有任务在等待
        从打印机队列中删除一个任务并将其分配给打印机
        从 second 中减去时间戳，以计算该任务的等待时间。
        将该任务的等待时间添加到列表中稍后处理。
        根据打印任务的页数，确定需要多少打印时间。
    打印机需要一秒打印，所以得从该任务的所需的等待时间减去一秒。
    如果任务已经完成，换句话说，所需的时间已经达到零，打印机空闲。
3、模拟完成后，从生成的等待时间列表中计算平均等待时间。
"""

# 模拟任务
# 任务: 随机生成页数，记录入队时间戳， 返回需要打印的页数，根据当前时间戳返回等待的时间
class Task:
    # 任务初始化
    def __init__(self, time):
        self.timestamp = time # time为任务创建时间，也即入队时间
        self.pages = random.randrange(1, 21) # 随机生成1到20页之间的页数

    # 获取任务的时间戳
    def getStamp(self):
        return self.timestamp

    # 获取任务的打印页数
    def getPages(self):
        return self.pages

    # 此任务打印开始前在队列中等待的时间
    def waitTime(self, currenttime):
        # currenttime为当前时间
        return currenttime - self.timestamp

# 模拟打印机
# 打印机: 设定打印速度，载入新任务并计算新任务剩余打印时间，打印
class Printer:
    # 打印机初始化
    def __init__(self, timeperpage):
        # timeperpage表示打印一页所需时间(单位为秒)
        self.timeperpage = timeperpage
        self.current_task = None   # 记录当前正在处理的任务
        self.remaining_time = 0 # 记录当前任务的剩余处理时间

    # 返回打印机是否空闲
    def isBusy(self):
        return self.current_task != None

    # 载入新任务
    def loadTask(self, next_task):
        self.current_task = next_task
        # 计算新任务的剩余处理时间(单位为秒)
        self.remaining_time = next_task.getPages() * self.timeperpage

    # 打印
    def tick(self):
        if self.current_task != None: # 有任务需要处理
            self.remaining_time = self.remaining_time - 1 # 将剩余时间减1
            if self.remaining_time <= 0: # 当前任务打印结束
                self.current_task = None
        else: # 空闲中
            pass

# 模拟打印
def simulation(total_time, timeperpage):
    # total_time为总的实验时间，timeperpage为每页打印所需要的时间
    waiting_time = [] # 记录每个任务的等待时间
    printer = Printer(timeperpage) # 初始化打印机
    waitQueue = Queue()  # 初始化任务等待队列

    for second in range(total_time):
        rand_num = random.randrange(1, 181)
        if rand_num == 180:
            new_task = Task(second) # 产生新任务
            waitQueue.enqueue(new_task) # 新任务进入等待队列

        if (not printer.isBusy()) and (not waitQueue.isEmpty()): # 如果打印机空闲并且有任务在队列
            new_task = waitQueue.dequeue() # 弹出最先进入的任务
            waiting_time.append(new_task.waitTime(second)) # 计算并记录等待时间
            printer.loadTask(new_task)

        printer.tick() # 打印

    average_time = sum(waiting_time) / len(waiting_time)
    print("Average Wait %6.2f secs %3d tasks remaing." % (average_time, waitQueue.size()))

def main():
    total_time = 3600 # 1小时
    
    # timeperpage = 1
    for i in range(10):
        simulation(total_time, timeperpage=1)
    print("--------------------------")
    # timeperpage = 5
    for i in range(10):
        simulation(total_time, timeperpage=5)
    print("--------------------------")
    # timeperpage = 10
    for i in range(10):
        simulation(total_time, timeperpage=10)


if __name__ == '__main__':
    main()

# 测试结果可知
# 每页所需时间越短，说明打印机速度越快，因而平均等待时间越短。这与实验数据是相符的。