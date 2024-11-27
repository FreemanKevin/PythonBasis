for i in range(8):
    print(i)

while True:
    num=eval('请输入一个整数：')
    if num//3:
        break

for i in range(-3,4):
    if i<0:
        print(' '*(-i)+'*'*(4+i))
    elif i>0:
        print(' '*3+'*'*(4-i))
    else:
        print('*'*7)

for i in 'python':
    for j in range(2):
        print(i,end='')
        if i=='h':
            break

i=0
while i<10:  # 0
    if i<1:
        print('hello')
        continue
    if i==5:
        print('world')
        break
    i+=1
