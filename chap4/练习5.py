import random
rand=random.randint(1,100)
count=1
while count<=10:
    number=eval(input('请输入一个一百以内的随机数：'))
    if number==rand:
        print('猜对了，真牛逼')
        break
    elif number >rand:
        print('猜大了，加油！')
    else:
        print('猜小了，加油！')
    count+=1
print('******************@系统评价@*******************')
if count<=3:
    print('你共计猜了',count,'次,','有点强')
elif count<=6:
    print('你共计猜了',count,'次,','还凑合')
else:
    print('你共计猜了',count,'次,','真垃圾')