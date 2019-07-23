from stack import Stack
# 进制转换

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

print(dec2bin(42))

# 扩展，10进制转换为任意进制
def baseConverter(decnumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decnumber > 0:
        rem = decnumber % base
        remstack.push(rem)
        decnumber = decnumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(256,16))