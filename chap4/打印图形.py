for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    print()
##################################
print('-'*20)
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()
##################################
print('-'*20)
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()
##################################
print('-'*20)
for i in range(1,6):
    for j in range(1,6-i):
        # print('&',end=''
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
##################################
print('-'*20)
row=eval(input('请输入行数(只能是奇数)：'))
while row%2==0:
    row=eval(input('请重新输入行数：')) #7
# 上半部
top_row=(row+1)//2 #行数
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        # print('&',end=''
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
# 下半部
bottom_row=row//2 # 3
for i in range(1,bottom_row+1): # 4 (1,2,3,4)
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):
        print('*',end='')
    print()
##################################
print('-'*20)
row=eval(input('请输入行数(只能是奇数)：'))
while row%2==0:
    row=eval(input('请重新输入行数：')) #7
# 上半部
top_row=(row+1)//2 #行数
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        # print('&',end=''
        print(' ',end='')
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
# 下半部
bottom_row=row//2 # 3
for i in range(1,bottom_row+1): # 4 (1,2,3,4)
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):
        if k==1 or k==2*bottom_row-2*i+2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()



