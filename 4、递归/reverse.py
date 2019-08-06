# 递归将字符串反转
def reverse(aString):
    if len(aString) <= 1:
        return aString
    else:
        return  aString[-1]+ reverse(aString[:-1])
        # # 或者下面这句
        # return reverse(aString[1:]) + aString[0]

assert reverse("hello") == "olleh", "error1"
assert reverse("l") == "l", "error2"
assert reverse("follow") == "wollof", "error3"
assert reverse("") == "", "error4"