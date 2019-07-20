"""无限猴子定理"""
import random
import string
from time import time

# 生成指定长度的随机字符串
def generate(strlen):

    # # 英文小写字母和空格组成的字符集
    # charset = string.ascii_lowercase+' ' 

    # 英文中可能出现的字符集合
    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~加空格 
    charset = string.ascii_letters + string.punctuation + " "  # 输出是一个字符串类型，总共85个
    charsetlen = len(charset)
    randchars = "".join(random.choice(charset) for _ in range(charsetlen))
    # randchars = ""
    # for i in range(strlen):
    #     randchars = randchars + charset[random.randrange(charsetlen)]
    return randchars

# 将随机生成的字符串与目标字符串进行比较，给出相似度
def score(goalstring, teststring):
    numSame = 0
    goallen = len(goalstring)
    for i in range(goallen):
        if goalstring[i] == teststring[i]:
            numSame += 1
    return numSame / goallen

# 重复多次后给出最相似的字符串
def main():

    goalstring = "methinks it is like a weasel"
    goal_len = len(goalstring)
    
    bestscore = 0
    bestsring = ""
    loopcount = 0 

    newstring = generate(goal_len)
    newscore = score(goalstring, newstring)
    while newscore < 1:
        if newscore > bestscore:
            print(newscore, newstring)
            bestscore = newscore
            bestsring = newstring
        newstring = generate(goal_len)
        newscore = score(goalstring, newstring)

        if loopcount % 1000000 == 0:
            print(bestscore, bestsring)
        loopcount += 1

main()