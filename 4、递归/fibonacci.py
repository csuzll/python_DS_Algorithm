# 递归求解斐波那契数列
# f(1)=1,f(2)=1,f(n)=f(n-1)+f(n-2)(n>=3)

# 生成一个指定序号的斐波那契额数
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))
# 下面的代码生成一个序列
fibolist = []
for i in range(1, 20):
    fibolist.append(fibonacci(i))
print(fibolist)


# 迭代(循环)求解斐波那契数列
def fibonacci_iter(n):
    if n <= 2:
        return [1] * n
    else:
        fibolist = [1, 1]
        for i in range(2, n):
            fibolist.append(fibolist[i-1] + fibolist[i-2])
    return fibolist
print(fibonacci_iter(19))

# 如果只是生成一个指定序号的斐波那契数，那么两种方法的时间复杂度是一样的。
# 但是如果生成的是一个序列的话，还是循环方法时间复杂度小，是O(n)；递归方法的时间复杂度是O(n^2)。
# 关键还是在于递归方法没有记录计算过的指定序号的斐波那契数的数值。