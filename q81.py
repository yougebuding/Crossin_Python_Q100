# Q81: 自守数 
# 如果某个数的平方的末尾几位等于这个数，那么就称这个数为自守数。
# 显然，5和6是一位自守数（5 * 5=25，6 * 6=36)。 25 * 25=625,76 * 76=5776，所以25和76是两位自守数。
# 求10000以内的自守数

l1 = []
for i in range(1,10001):
    a = i ** 2
    b = len(str(i))
    a = str(a)
    if a[-b:] == str(i):
        l1.append(i)

[print(i) for i in l1]
