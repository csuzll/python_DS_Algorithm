class LogicGate:
    """逻辑门总类"""
    def __init__(self, n):

        # n为逻辑门的标记
        self.name = n 
        # self.output代表逻辑门的输出
        self.output = None

    def getLabel(self):
        return self.name

    def getOutput(self):
        # 可将performGateLogic看作接口，参数self会自动指向实现了performGateLogic方法的子类。
        self.output = self.performGateLogic() 
        return self.output

class BinaryGate(LogicGate):
    """具有两个输入引脚的逻辑门"""
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)

        # 输入引脚A
        self.pinA = None
        # 输入引脚B
        self.pinB = None

    """
       由于逻辑门的引脚输入不一定全部来自于外部，
       也有可能来自于其他逻辑门的输出，
       因此，逻辑门的输入有两种方式。
    """

    def getPinA(self):
        if self.pinA == None:
            # 用户输入的pinA值
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            # 上一个逻辑门的输出值
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            # 用户输入的pinB值
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            # 上一个逻辑门的输出值
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        """有其它逻辑门连接该门的输入"""
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):
    """与门"""
    def __init__(self, n):
        super(AndGate, self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    """或门"""
    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class NandGate(BinaryGate):
    """与非门"""
    def __init__(self,n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 and b==1:
            return 0
        else:
            return 1

class NorGate(BinaryGate):
    """或非门"""
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==0 and b==0:
            return 1
        else:
            return 0
        
class XorGate(BinaryGate):
    """异或门"""
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1

class UnaryGate(LogicGate):
    """单个输入引脚的逻辑门"""
    def __init__(self, n):
        super(UnaryGate, self).__init__(n)

        # 仅此一个输入引脚pin
        self.pin = None

    """
       由于逻辑门的引脚输入不一定全部来自于外部，
       也有可能来自于其他门的输出，
       因此，逻辑门的输入有两种方式。
    """

    def getPin(self):
        if self.pin == None:
            # 用户输入的pin值
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            # 上一个逻辑电路的输出
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        """有其他逻辑门连接该门的输入"""
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class NotGate(UnaryGate):
    """非门"""
    def __init__(self,n):
        super(NotGate, self).__init__(n)

    # 实现非门逻辑
    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

class Connector:
    """引线类: 在逻辑门之间建立connection"""
    def __init__(self, fgate, tgate):

        self.fromgate = fgate # 一个连接的开始逻辑门
        self.togate = tgate # 一个连接的结束逻辑门


        """
            将tgate的这个逻辑门类的pin指向一个connector的实例，
            也就意味着BinaryGate或者UnaryGate类中的self.pin指向了一个connector的实例
            因此，在BinaryGate或者UnaryGate类中的self.pin可以调用getFrom()方法
        """
        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


# 测试
def main():

    # g1 = AndGate("G1")
    # g2 = AndGate("G2")
    # g3 = OrGate("G3")
    g4 = NotGate("G4")
    # c1 = Connector(g1, g3)
    # c2 = Connector(g2, g3)
    # c3 = Connector(g3, g4)
    # # 以上共同构造了一个逻辑电路
    # """
    # ===G1——
    #        |——G3——G4——
    # ===G2——
    # """
    # print(g4.getOutput())

    g5 = NandGate("G5")
    g6 = NorGate("G6")
    g7 = XorGate("G7")
    c4 = Connector(g5, g7)
    c5 = Connector(g6, g7)
    c6 = Connector(g7, g4)
    # 以上共同构造了一个逻辑电路
    """
    ===G5——
           |——G7——G4——
    ===G6——
    """
    print(g4.getOutput())


if __name__=="__main__":
    main()


# 一个测试
# Enter Pin A input for gate G5-->1
# Enter Pin B input for gate G5-->1
# Enter Pin A input for gate G6-->1
# Enter Pin B input for gate G6-->1
# 1