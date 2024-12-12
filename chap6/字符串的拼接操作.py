s1='hello'
s2='world'
# 法1：使用加号进行拼接
print(s1+s2)
# 法2：使用字符串的join()方法
print(''.join([s1,s2]))
print('&'.join(['python','java','rust','go','ruby']))
print('--'.join(['爱','你','亿','万','年']))
# 法3：直接拼接
print('hello''world')
# 法4：使用格式化字符串进行拼接
print('%s%s' % (s1,s2)) # 占位符
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2)) # 占位符
