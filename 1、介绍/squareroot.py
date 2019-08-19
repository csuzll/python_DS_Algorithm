# 求平方根
def squareroot(n):
    root = n / 2
    for k in range(20):
        root = (1/2) * (root + n / root)

    return root

if __name__ == '__main__':
    res = squareroot(3)
    print(res)