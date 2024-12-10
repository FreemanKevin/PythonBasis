# 创建空集合
s=set()
# 设置循环次数
for i in range(1,6):
    info=input(f'请输入第{i}位好有的手机号：')
    s.add(info)
# 遍历集合
for item in s:
    print(item)
