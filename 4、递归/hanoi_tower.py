# 汉诺塔问题

# 从fromPole借助withPole移动到toPole上，第四个参数是中间杆
def moveTower(height, fromPole, toPole, withPole): 
    if height == 1:
        # 1个盘子时，直接移动
        print("moving Plate %d from %s to %s" % (height, fromPole, toPole))
    else:
        # 将height-1从fromPole借助toPole移动到withPole
        moveTower(height-1, fromPole, withPole, toPole)
        # 将height从fromPole移动到toPole
        # 打印出每次单片的移动
        print("moving Plate %d from %s to %s" % (height, fromPole, toPole))
        # 将height-1从withPole借助fromPole移动到toPole
        moveTower(height-1, withPole, toPole, fromPole)

moveTower(3,"A","B","C")