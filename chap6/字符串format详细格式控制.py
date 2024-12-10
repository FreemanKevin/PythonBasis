s='helloworld'
print('{0:*<20}'.format(s)) #0,format起始位 : 引导符号 *填充符号，只能是单个 <左对齐>右对齐^居中对齐 20 长度
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))
print(s.center(20,'*')) # 居中对齐

print('{0:.2f}'.format(312345552323.23)) # 保留2位小数
print('{0:.4}'.format('312345552323')) #保留4位整数

a=242 # 整数类型
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x},十六进制:{0:X}'.format(a))

b=3.1415926 # 浮点类型
print('{0:.2f},{0:.2E},{0:2e},{0:.2%}'.format(b))