from LogicGate import LogicGate, BinaryGate, UnaryGate, XorGate, AndGate, OrGate, Connector

class InGate(UnaryGate):
    """输入门"""
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin():
            return 1
        else:
            return 0

class FullAdder(LogicGate):
    """全加法器"""
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.in1 = InGate("I1")
        self.in2 = InGate("I2")
        self.in3 = InGate("I3")
        self.xor1 = XorGate("X1")
        self.xor2 = XorGate("X3")
        self.and1 = AndGate("A1")
        self.and2 = AndGate("A2")
        self.or1 = OrGate("O1")
        c1 = Connector(self.in1, self.xor1)
        c2 = Connector(self.in2, self.xor1)
        c3 = Connector(self.xor1, self.xor2)
        c4 = Connector(self.in3, self.xor2)
        c5 = Connector(self.xor1, self.and1)
        c6 = Connector(self.in3, self.and1)
        c7 = Connector(self.in1, self.and2)
        c8 = Connector(self.in2, self.and2)
        c9 = Connector(self.and1, self.or1)
        c10 = Connector(self.and2, self.or1)


    def setNextPin(self, source):
        if self.in1.pin == None:
            self.in1.pin = source
        elif self.in2.pin == None:
            self.in2.pin = source
        elif self.in3.pin == None:
            self.in3.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

    def getSumAndCarry(self):
        return self.xor2.getOutput(), self.or1.getOutput()

def main():
    f1 = FullAdder("F1")
    print(f1.getSumAndCarry())

if __name__ == "__main__":
    main()