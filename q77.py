# Q77: 约瑟夫生者死者小游戏
# 问题描述：30 个人在一条船上，超载，需要 15 人下船。
# 于是人们排成一队，排队的位置即为他们的编号。
# 报数，从 1 开始，数到 9 的人下船。如此循环，直到船上仅剩 15 人为止，
# 问都有哪些编号的人下船了呢？

l1 = [i for i in range(1,31)]
l2 = [i for i in range(1,31)]
l3 = []
while len(l1) > 15:
    l1 = l1[9:] + l1[:8]

for i in l2:
    if i not in l1:
        l3.append(i)

print(l3)
