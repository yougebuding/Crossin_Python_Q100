# Q83: 卡布列克常数
# 任意一个不是用完全相同数字组成的四位数，如果对它们的每位数字重新排序，组成一个较大的数和一个较小的数，
# 然后用较大的数减去较小数，不够四位数时补零，
# 类推下去，最后将变成一个固定的数：6174，这就是卡布列克常数。
# 例如：
# 4321-1234=3087
# 8730-378=8352
# 8532-2358=6174
# 7641-1467=6174
# 编写程序验证卡布列克常数。

def num(n):
    if n == 6174:
        return 6174
    else:
        l1 = str(n)
        l2 = sorted(l1)
        l3 = sorted(l1,reverse=True)
        a = int(''.join(l3)) - int(''.join(l2))
        return num(a)
print(num(9176))
