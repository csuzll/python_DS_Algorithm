# 使用stack实现字符串反转

from stack import Stack

def revstring(mystr):
    s = Stack()
    revstr = ""

    for c in mystr:
        s.push(c)
    while not s.isEmpty():
        revstr = revstr + s.pop()
    return revstr

if __name__ == '__main__':
    # 测试
    assert revstring("apple") == "elppa", "apple Error"
    assert revstring("x") == "x", "x Error"
    assert revstring("1234567890") == "0987654321", "error"