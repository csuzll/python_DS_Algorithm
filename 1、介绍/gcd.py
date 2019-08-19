# 求两个数的最大公约数
def gcd(m, n):
    while(n!=0):
        rem = m % n
        m = n
        n = rem
    return m

def main():
    m, n =1989, -1590
    maxnum = gcd(m, n)
    print(maxnum)

if __name__ == '__main__':
    main()