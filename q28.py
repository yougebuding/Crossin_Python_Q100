# Q28: 根据输入年份判断二月的天数
# 实际为判断闰年(分析)：百年除以400，非百年除以4，能除尽则为闰年

a = int(input('请输入一个年份的整数:'))
if a % 100 == 0:
    if a % 400 == 0:
        print('%d 是闰年，2月的天数为 29天' % a)
    else:
        print('%d 不是闰年，2月的天数为 28天' % a)
elif a % 4 == 0:
    print('%d 是闰年，2月的天数为 29天' % a)
else:
    print('%d 不是闰年，2月的天数为 28天' % a)
