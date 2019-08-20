# 进制转换（10进制转换为任意进制，且10进制数为大于0的正整数）

from stack import Stack

# 10进制转换为2进制，通过被2除的余数获取  
def dec2bin(decnumber):
    remstack = Stack()

    while decnumber > 0:
        rem = decnumber % 2
        remstack.push(rem)
        decnumber = decnumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    return binString

# 扩展，10进制转换为任意进制
def baseConverter(decnumber, base):
    
    remstack = Stack()

    while decnumber > 0:
        rem = decnumber % base
        remstack.push(rem)
        decnumber = decnumber // base

    digits = "0123456789ABCDEF"
    newString = ""

    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    if base == 8:
        newString = "0" + newString
    elif base == 16:
        newString = "0x" + newString

    return newString

if __name__ == '__main__':
    print(dec2bin(256))
    print(baseConverter(256, 10))
    print(baseConverter(256, 2))
    print(baseConverter(256, 8))
    print(baseConverter(256, 16))