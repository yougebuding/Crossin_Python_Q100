# Q9: 按相关图形打印
# 问题描述：请使用 * 打印出如下
# *
# **
# ***
# ****
# *****
# 第一种做法
for i in range(1,6):
    print('*' * i)

# 第二种做法
[print('*'*i) for i in range(1,6)]
