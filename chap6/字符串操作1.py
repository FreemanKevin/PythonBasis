s='HelloWorld'
# 字符串的替换
net_s=s.replace('o','你好',1)
print(net_s)

# 字符串在指定的宽度范围内居中
print(s)
print(s.center(20))
print(s.center(20,'*'))

s='    Hello    World  '
print(s.strip()) # 去除字符串左右的空格
print(s.lstrip()) # 去除字符串左侧空格
print(s.rstrip()) # 去除右侧空格

s3='dl-Helloworld'
print(s3.strip('ld'))  # 去除指定字符串,与顺序无关
print(s3.lstrip('ld')) # 去除左侧指定字符串
print(s3.rstrip('ld')) # 去除右侧指定字符串



