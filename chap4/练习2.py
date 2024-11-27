year=eval(input('请输入年份：'))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,'年是闰年.')
else:
    print(year,'年是平年.')


#
num=input('请输入10086查询功能代号(0-3):')
match num:
    case '0':
        print('退出自助查询系统')
    case '1':
        print('显示当前余额：99999999999999999999999999美刀')
    case '2':
        print('显示当前的剩余流量：999999999999999999999999999G')
    case '3':
        print('显示当前的剩余通话时间：9999999999999999999min')