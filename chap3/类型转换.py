x=10
y=3
z=x/3
print(z,type(z))
#
print('float类型转换成int类型',int(3.14)) # float转int之后只会保留整数部分
print('float类型转换成int类型',int(3.9))
print('float类型转换成int类型',int(-3.14))
print('float类型转换成int类型',int(-3.9))
#
print('int类型转换成float类型',float(3))
print(int(3.14)+int(3.2))
print(int('100')+int('200'))
# print(int('19a'))  # ValueError: invalid literal
# print(int('3.14')) # ValueError: invalid literal

# chr()-ord()
print(ord('杨'))  # unicode 字符中对应的整数
print(chr(26472)) # 整数对应的unicode 字符

# 进制转换
print('十进制转换成十六进制：',hex(26472))
print('十进制转换成八进制：',oct(26472))
print('十进制转换成二进制：',bin(26472))





