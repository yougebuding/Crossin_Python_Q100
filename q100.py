# Q100: 百鸡百钱 
# “百鸡问题”：鸡翁一，值钱五，鸡母一，值钱三，鸡雏三，值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
# 即，公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱。
# 如果用100文钱买100只鸡，那么公鸡、母鸡和小鸡各应该买多少只呢？

l = []
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i + j + k == 100 and 5*i + 3*j + k/3 == 100:
                print('可买 %d 只公鸡；可买 %d 只母鸡；可买 %d 只小鸡' % (i,j,k))
