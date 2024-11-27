s=0
i=1
while i<20:
    s+=i
    if s >20:
        print('累加和大于20的当前数是：',i)
        break
    i+=1
print('--------------------')
i=0
while i<3:
    username=input("请输入用户名：")
    password=input("请输入用户密码：")
    if username=='admin' and password=='123':
        print('登录成功')
        break
    else:
        if i<2:
            print('请重新输入，你还有',2-i,'次机会')
    i+=1
else:
    print('三次均输入错误，账户已经被锁定！')

print('--------------------')
for i in 'hello':
    if i=='e':
        break
    print(i)
print('--------------------')
for i in range(3):
    username=input("请输入用户名：")
    password=input("请输入用户密码：")
    if username=='admin' and password=='123':
        print('登录成功')
        break
    else:
        if i<2:
            print('请重新输入，你还有',2-i,'次机会')
    i+=1
else:
    print('三次均输入错误，账户已经被锁定！')
