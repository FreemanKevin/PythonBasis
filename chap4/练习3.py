answer='y'
while answer=='y':
    print('---------------欢迎使用10086自助查询功能---------------')
    print('0.退出系统')
    print('1.查询余额')
    print('2.查询流量')
    print('3.查询通话')
    choice=eval(input('请输入查询代码：'))
    if choice==0:
        print('退出系统')
        break
    elif choice==1:
        print('当前账户余额为：200美刀.')
    elif choice==2:
        print('当前剩余流量为：20GB.')
    elif choice==3:
        print('当前剩余通话时长：300分钟')
    else:
        print('您的输入有误，请重新输入')
    answer=input('您是否还需要继续执行？y/n ' )
else:
    print('退出系统，感谢您的使用。')