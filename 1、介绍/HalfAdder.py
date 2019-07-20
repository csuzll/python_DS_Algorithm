from LogicGate import BinaryGate

class HalfAdder(BinaryGate):
    """半加法器"""
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == b:
            SUM = 0
        else:
            SUM =1

        if a == 1 and b == 1:
            CARRY = 1
        else:
            CARRY = 0

        return SUM, CARRY

def main():

    h1 = HalfAdder("H1")
    print(h1.getOutput())

if __name__=="__main__":
    main()
