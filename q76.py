# Q76: 输出 1 到 10000 之间的阿姆斯特朗数
# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 
# 例如1^3 + 5^3 + 3^3 = 153。
# eg，1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407

for i in range(1,10001):
    s = str(i)
    a = len(s)
    if i == sum([int(j) ** a for j in s]):
        print(i)
