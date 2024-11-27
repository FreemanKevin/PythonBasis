lst=['hello','world','php','python']

for item in lst:
    print(item)
print('-'*20)
for i in range(0,len(lst)):
    print(i,'--->',lst[i])  # 这里i 是索引
print('-'*20)
for index,item in enumerate(lst):
    print(index,item)  # 这里index 是序号，非索引
print('-'*20)
for index,item in enumerate(lst,start=1):
    print(index,item) # 将这里的index 序号改为1

