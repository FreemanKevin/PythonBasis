lst=[88,89,90,00,90]
print(lst)
print('200'+str(00)) # 00 字符串之后会变0

for index in range(len(lst)):
    if str(lst[index])!='0':
        lst[index]='19'+str(lst[index])
    else:
        lst[index]='200'+str(lst[index])
print('修改后的年份列表：',lst)

