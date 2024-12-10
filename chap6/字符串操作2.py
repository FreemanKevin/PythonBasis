s1='HelloWorld'
new_s2=s1.lower() # 小写
print(new_s2)

new_s3=s1.upper() # 大写
print(new_s3)

e_mail='good@gmail.com'
name=e_mail.split('@')  # 字符串中的分隔符
print('邮箱名称：',name[0],'邮箱域名：',name[1])

print('s1 中字符o出现的次数：',s1.count('o'))
print('s1 中字符o首次出现的索引编号位：',s1.find('o'))
print(s1.find('p'))  # 查找不存在的字符时，没有找到就是-1
print(s1.index('o'))
# print(s1.index('p')) # ValueError: substring not found

print(s1.startswith('H'))
print(s1.startswith('P')) # 判断前缀
print('demo.py'.endswith('.py')) # 判断后缀
print('demo.txt'.endswith('.txt'))
