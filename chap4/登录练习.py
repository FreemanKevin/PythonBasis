i=0
while i<3:
    username=input('请输入你的用户名：')
    password=input('请输入你的密码：')
    if username=='admin' and password=='123':
        print('登录成功')
        i=8
    else:
        if i<2:
            print('用户名或密码不正确，你还有',2-i,'次机会')
        i+=1
if i==3:
    print('三次用户名密码均输入错误，你目前已经无法登录。')