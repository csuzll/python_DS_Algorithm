# 判断字符串是不是回文

def removeWhite(aString):
    # 字符串中要去掉的字符
    excludes = ("'", ",", ";", ".", " ")
    # 字符中的字母全部大写
    return "".join(ch.upper() for ch in aString if ch not in excludes)

def isPalindrome(aString):
    aString = removeWhite(aString)

    if len(aString) <= 1:
        return True
    else:
        return aString[0] == aString[-1] and isPalindrome(aString[1:-1])

assert isPalindrome("x") == True, "error1"
assert isPalindrome("radar") == True, "error2"
assert isPalindrome("hello") == False, "error3"
assert isPalindrome("") == True, "error4"
assert isPalindrome("hannah") == True, "error5"
assert isPalindrome("madam i'm adam") == True, "error6"