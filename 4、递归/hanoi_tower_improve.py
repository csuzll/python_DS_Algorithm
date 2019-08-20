# 改进汉诺塔算法，使用3个栈记录三个柱子的实时情况
class Tower:
    def __init__(self, name):
        self.name = name
        self.stack = []
        
def get_tower_by_name(name, ts):
    for t in ts:
        if t.name == name:
            return t

def moveTower(height,fromPole, toPole, withPole):
    """宏观上的移动"""
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole, withPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fromPole, toPole, withPole):
    """具体移动一个盘子"""
    print("moving disk from", fromPole.name, "to", toPole.name)
    toPole.stack.append(fromPole.stack.pop())
    print("Tower A: ", get_tower_by_name("A", [fromPole, toPole, withPole]).stack)
    print("Tower B: ", get_tower_by_name("B", [fromPole, toPole, withPole]).stack)
    print("Tower C: ", get_tower_by_name("C", [fromPole, toPole, withPole]).stack)

def main_hanoi(height):
    t_from = Tower("A")
    t_to = Tower("B")
    t_with = Tower("C")
    t_from.stack = list(range(height, 0, -1))
    moveTower(height, t_from, t_to, t_with)
    
if __name__ == '__main__':
    main_hanoi(3)