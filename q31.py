# Q31: 输入圆的半径求计算圆的面积
# 输入圆的半径求计算圆的面积，pi = 3.142
# 分析：圆的面积公式: pi*r*r

from math import pi as math_pi
a = float(input('请输入圆的半径:'))
s = math_pi * a * a
print('该圆的面积为(保留2位小数):%.2f' % s)
