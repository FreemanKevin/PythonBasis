# PythonBasis



## 1 基础语法



### 1.1 print函数

语法格式

```python
print(value,xxx,sep='', end='\n',file=None)
```



#### 实例1

```py
a=10
b=20
print(90)
print(a*b)
print('welcome to china!')
print("welcome to china!")
print("""welcome to china!""")
print('''welcome to china!''')
```



#### 实例2

```py
c=10
d=20
print(c,d,'要么出众，要么出局！')
```





#### 实例3

```py
print(b)
print(chr(98))
print('C')
print(chr(67))
print(8)
print(chr(56))
print('[')
print(chr(91))
```





#### 实例4

```py
print(ord('北'))
print(ord('京'))
print(chr(21271),chr(20140))
```







#### 实例5

```py
fp=open('note.txt','w')
print('welcome to china', file=fp)

# 
fp=open('test.txt','w',encoding='utf-8')
print('人生苦短，我用PY',file=fp)
fp.close()
```





#### 实例6

```py
print('北京',end='-->')
print('北京')
print('北京欢迎您！'+'2008')
```





### 1.2 int函数

```py
a=int(input('请输入你的幸运数字：'))
print('您的幸运数字是：',a)

# 
name=input('请输入姓名：')
age=input('请输入年龄：')
motto=input('请输入座右铭：')
print('-----------------自我介绍------------------')
print('姓名',name)
print('年龄',age)
print('座右铭',motto)
```









### 1.3 注释

```py
# encoding=gbk # 这是文件编码注释，只能放在文件的首行
# encoding=utf-8  # 只能放在文件的首行

#
print('hello world') # 这是单行注释

#
"""
第一行：xxx  这是多行注释
第二行：xxx
第三行：xxx
"""

'''
第一行：xxx
第二行：xxx
第三行：xxx
'''
```



### 1.4 缩进

```python
print('') # 一般代码不缩进

# 类
class Students():
    pass # 缩进

# 函数
def fun():
    pass # 缩进
```



### 1.5 关键字

```python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
```



### 1.6 标识符

```python
# 1.模块名、包名尽量短小，并且全部使用小写字母
# 2.模块名，可以使用下划线，比如：grame_main
# 3.包名，可以使用.，比如：com.mypython,不推荐使用com_mypython
# 4.类名，使用Pascal 风格命名，比如：MyClass
# 5.模块内部的类，使用_ + 使用Pascal 风格命名，比如：_InnerMyClass

# 6._开头的模块变量无法被导入，是受保护的。
# 7.__开头的类或方法是私有的。
# 8.__开头和结尾的类或者函数，是python专用标识。
```



### 1.7 变量

>*警告：*
>
>1. 务必谨慎使用小写字母`i` 和大写字母`O`

```python
luck_number=8
my_name='zhan'
print('luck_number的数据类型是：',type(luck_number))
print(my_name,'的幸运数字是：',luck_number)

luck_number='welcome to china'
print('luck_number的数据类型是：',type(luck_number))

no=number=2017
print(id(no))
print(id(number))
```







### 1.8 常量

一般使用大写字母标识，不希望被修改。

```python
pi=3.1415926 # 变量，可以修改
PI=3.1415926 # 常量，不可修改
```





### 1.9 进制

```python
num=987 # 10进制
num2=0b101010 # 二进制
num3=0o765   # 八进制
num4=0x87ABF  # 16 进制
print(num,num2,num3,num4)
```







### 1.10 浮点数

```python
a=10
b=10.0
c=1.99e1413 # 科学计数法

print('a的数据类型',type(a))
print('b的数据类型',type(b))
print('c的数据类型',type(c))
```





### 1.11 复数

**复数的基本概念**

在Python中，复数（complex numbers）由实部和虚部组成，形式为 `a + bj`，其中：

- `a` 是实部（real part）
- `b` 是虚部（imaginary part）
- `j` 代表虚数单位（通常数学上用 `i` 表示，但Python中用 `j`）

例如，`3 + 4j` 就是一个复数，3 是实部，4 是虚部。





**Python中的复数表示**

- 直接赋值：`c = 3 + 4j`

- 使用 `complex` 函数：`c = complex(3, 4)`

  

**复数的操作**

Python支持对复数进行基本的数学运算，如加法、减法、乘法、除法、幂运算等：

```python
d=1+2j
e=2-3j
print('实数部分：',d.real)
print('虚数部分：',d.imag)
print(d+e)
```





### 1.12 字符串

#### 实例1

```python
name='zhang'
address='广东省广州市白云区香奈儿街费力大厦B座2楼208'
link1='''\n地址：广东省广州市天河区王璐璐街道田丽华源C栋9楼29D
姓名：王爱仁
电话：1980099081
'''
link2="""\n地址：广东省广州市天河区王璐璐街道田丽华源C栋9楼29D
姓名：王爱仁
电话：1980099081
"""
print(name,address,link1,link2)
```



#### 实例2

```python
print('北京')
print('北京欢迎你！')
print('------------')
print('北京欢迎你！')
print('hello')
print('hell\no')
print('helloworld')
print('hello\tworld')#tab 长度取决于前面的字符，英文更长一点
print('北京欢迎你！')
print('北京欢迎\t你！')
print('老实说：好好学习，天天向上')
print('老实说：\'好好学习,天天向上\'')
print('老实说：\'好好学习,天天向上\'')
print('老实说：\"好好学习，天天向上\"')
print(r'老实说：\'好好学习,天天向上\'') # r、R 原字符，取消转义字符特殊含义
print(R'老实说：\"好好学习，天天向上\"')
```





#### 实例3

字符串的切片与索引

```python
s='HELLOWORLD'
print(s[:])
print(s[0:10])
print(s[2:-1])
print(s[:-1])
print(s[-1])
print(s[5:])
```





#### 实例4

```python
a='2024年'
b='北京冬奥会'

print(a+b)
print(a*2)
print('202' in a)
print('201' in a)
```



### 1.13 布尔值

```python
x=True
print(x)
print(x+10)
print(type(x))
print(-x+10)
print(False+10)

print(bool(0))  # 非零，非空，非None为true
print(bool(0.0))
print(bool(-0))
print(bool(''))
print(bool('hello'))
print(bool(-1))
print(bool('北京欢迎你'))
print(bool(True))
print(bool(False))
print(bool(None))

```





### 1.14 类型转换

```python
x=10
y=3
z=x/3
print(z,type(z))
#
print('float类型转换成int类型',int(3.14)) # float转int之后只会保留整数部分
print('float类型转换成int类型',int(3.9))
print('float类型转换成int类型',int(-3.14))
print('float类型转换成int类型',int(-3.9))
#
print('int类型转换成float类型',float(3))
print(int(3.14)+int(3.2))
print(int('100')+int('200'))
# print(int('19a'))  # ValueError: invalid literal
# print(int('3.14')) # ValueError: invalid literal

# chr()-ord()
print(ord('杨'))  # unicode 字符中对应的整数
print(chr(26472)) # 整数对应的unicode 字符

# 进制转换
print('十进制转换成十六进制：',hex(26472))
print('十进制转换成八进制：',oct(26472))
print('十进制转换成二进制：',bin(26472))
```





### 1.15 eval函数

```python
s='3.13+3'
print(s,type(s))
x=eval(s)
print(x,type(x))

# int
age=eval(input('请输入你的年龄：'))
print(age,type(age))
# float
height=eval(input('请输入你的年龄：'))
print(height,type(height))

#
hello='北京欢迎您'
print(hello)
print(eval('hello'))
# print(eval(hello)) # NameError: name '北京欢迎您' is not defined   字符串在这里没被定义
```





### 1.16 算术运算符

运算优先级：幂运算 > 乘除 > 加减



> ## 除法与整除的区别
>
> ### 除法
>
> - **定义:** 将一个数平均分成若干份，求每份是多少或分成了多少份的运算。
> - **结果:** 可以是整数、小数或分数，即包含了余数。
> - **应用:** 广泛应用于各种计算，包括分数、小数运算、比例分配等。
>
> **示例:**
>
> - 10 / 2 = 5  （将10平均分成2份，每份是5）
> - 10 / 3 = 3.333... （将10平均分成3份，每份是3.333...）
>
> ### 整除
>
> - **定义:** 一个整数能够被另一个整数除尽（没有余数），即商也是整数。
> - **结果:** 只能是整数。
> - **应用:** 在数学理论、编程、以及需要精确整数结果的场景中经常使用。
>
> **示例:**
>
> - 10 // 2 = 5  （10能被2整除，商是5）
> - 10 // 3 = 3  （10不能被3整除，取商的整数部分，即3）

```python
print('加法：',1+1)
print('减法：',1-1)
print('乘法：',1*2)
print('除法：',10/2)
print('整除：',10//3)
print('取余：',10%3)
print('幂运算：',2**4)
# print('除法：',10/0) # ZeroDivisionError: division by zero
```





### 1.17 赋值运算符

```python
x=20
y=10
x=x+y
print(x,type(x))

#
a=1
b=2
a+=b
print(a,type(a))
b-=a
print(b,type(b))

#
c=10
d=2
c*=d
print(c,type(c))
d/=c
print(d,type(d))

#
e=10
f=20
e%=f
print(e,type(e))
f//=e
print(f,type(f))

#
g=2
h=3
g**=h
print(g,type(g))

# 链式赋值
a=b=c=100
print(a,b,c)
# 系列解包赋值
a,b=10,20
print(a,b)
a,b=b,a
print(a,b)
```





### 1.18 比较运算符

```python
print('98小于90吗？',98<90)
print('98大于90吗？',98>90)
print('98等于90吗？',98==90)
print('98不等于90吗？',98!=90)
print('98小于等于90吗？',98<=90)
print('98小于等于98吗？',98<=98)
print('98大于等于90吗？',98>=90)

```





### 1.19 逻辑运算符

> 1. 逻辑与，and, 从左到右计算，一个为假都是假
> 2. 逻辑或，or，从左到右计算，一个为真都是真
> 3. 逻辑非，not, 从左到右计算



```python
print(True and False)
print(False and False)
print(False and True)
print(True and True)
print(False and False)
print('-'*20)

print(8>7 and 6>5)
print(8<7 and 6>5)
print(8>7 and 6<5)
print(8<7 and 6<5)
print('-'*20)

print(True or False)
print(False or True)
print(True or True)
print(False or False)
print('-'*20)

print(9>8 or 8>10)
# print(10/0 or 10<10) # ZeroDivisionError: division by zero
print(10<11 or 10/0)
print('-'*20)

print(not True)
print(not False)
print(not 10<0)
print(not (10>0))
print('-'*20)
```



### 1.20 字符串练习

> 白板工具：https://miro.com/app/board

```python
number=eval(input('请输入四位数的整数：'))
print('个位上面的数字：',number%10)
print('十位上面的数字：',number//10%10)
print('百位上面的数字：',number//100%10)
print('千位上面的数字：',number//1000)
print('-'*40)
number=input('请输入四位数的整数：')
print('个位上面的数字：',number[-1])
print('十位上面的数字：',number[-2])
print('百位上面的数字：',number[1])
print('千位上面的数字：',number[0])

mom_height=eval(input("请输入母亲的身高："))
father_height=eval(input("请输入父亲的身高："))
son_height=(mom_height+father_height)*0.54
print("您儿子的身高预计是：",son_height)

```





### 1.21 if双分支结构

```python
number=eval(input('请输入你的数字：'))
if number==123456:
    print('中奖')
else:
    print("谢谢惠顾")

# 使用条件表达式简化
print('中奖') if number==123456 else print('谢谢惠顾')
```





### 1.22 if多分支结构

```python
score=eval(input("请输入您的成绩："))
if score <0 or score >100:
    print("输入有误")
elif score == 100:
    print("满分")
elif 60 <= score <100:
    print("通过")
else:
    print("未通过")
```





### 1.22 if嵌套结构

```python
answer=input('请问您喝酒了吗？')
if answer=='y':
    proof=eval(input("请输入酒精含量："))
    if proof<=20:
        print("你可以开车")
    else:
        print("你不可以开车")
else:
    print("请开走，Goodbye!")
```





### 1.23 模式匹配

```python
score=input('请输入成绩：')
match score:  # python3.11+ 新特性
    case 'A':
        print('优秀')
    case 'B':
        print('及格')
    case 'C':
        print('勉强')
    case 'D':
        print('未通过')
```







### 1.24 for循环

```python
for i in "hello":
    print(i)

for i in range(1,11):
    print(i)

s=0
for i in range(1,11):
    s+=i
print(s)

"""
153=5**3+3**3+1**3
"""
for i in range(100,1000):
    gn=i%10
    sn=i//10%10
    bn=i//100
    if i==gn**3+sn**3+bn**3:
        print(i)

```



### 1.25 while循环

```python
answer=input("今天要上课吗？y/n")
while answer=='y':
    print("good study, day day up")
    answer=input("今天要上课吗？y/n")

s=0
i=1
while i<=100:
    s+=i
    i+=1
print(s)

# ---------------------------
s=0
i=1
while i<=100:
    s+=i
    i+=1
else:
    print(s)
```







#### 练习1

```python
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
```







#### 练习2

```python
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
```







### 1.26 break退出循环

```python
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
```





### 1.27 continue跳过本次循环

```python
s=0
i=1
while i<=100:
    if i%2==1:
        i+=1
        continue
    s+=i
    i+=1
print("一百以内的偶数之和：",s)
#
s=0
i=1
for i in range(1,101):
    if i % 2 == 1:
        i += 1
        continue
    s += i
print("一百以内的偶数之和：", s)
```





### 1.28 pass空语句

```python
if True:
    pass
for i in range(10):
    pass
while True:
    pass
```



#### 练习1

```python
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

    
year=eval(input('请输入年份：'))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,'年是闰年.')
else:
    print(year,'年是平年.')

    
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
        
#
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
```



#### 练习2

```python
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
```



### 1.29 索引

```python
s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
```



### 1.30 切片

```python
s='HelloWorld' # 0-4 5-9
s1=s[0:5:2]
print(s1)
print(s[:5:1])
print(s[:5:])
print(s[:5:])
print(s[5:])
print(s[::2])
print(s[::-1])
print(s[-1:-11:-1])
```



### 1.31 序列操作

```python
s='helloworld'
print('e在'+s+'中吗？',('e'in s))
print('v在'+s+'中吗？',('v'in s))

print('e不在'+s+'中吗？',('e'not in s))
print('v不在'+s+'中吗？',('v'not in s))

print('len()',len(s))
print('max()',max(s)) # 'w' 在字符串"helloworld"中是ASCII值最大的字符，因为它在字母表中比其他字符都靠后。 ASCII值为119
print('min()',min(s)) # 'd' 是ASCII值最小的字符，因为它在字母表中比其他字符都靠前。ASCII值为100

print('s.index()', s.index('h'))
print('s.count()', s.count('l'))
```



### 1.32 列表

```python
lst=['hello','world',92,100.01,20.4]
lst2=list('helloworld')
lst3=list(range(1,10,2))

print(lst,'\n',lst2,'\n',lst3)
print(lst*3)
print(lst+lst2+lst3)
print(len(lst))
print(max(lst3))
print(min(lst3))
print(lst2.count('o'))
```



#### 列表遍历

```python
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

```



#### 列表数据增删

```python
lst=['hello','world','python']
print('这里是原始数据：',lst,id(lst))
print('---------------------')
lst.append('sql')
print('增加数据之后：',lst,id(lst))
print('---------------------')
lst.insert(1,100)
print('增加数据之后：',lst,id(lst))
print('---------------------')
lst.remove('world')
print('移除数据之后：',lst,id(lst))
print('---------------------')
lst.pop(1)
print('移除数据之后：',lst,id(lst))
print('---------------------')
# lst.clear()
# print('清除所有数据之后：',lst,id(lst))
lst.reverse()
print('反转数据之后：',lst,id(lst))
print('---------------------')
new_lst=lst.copy()
print('这里是原始数据的副本：',new_lst,id(new_lst))
print('---------------------')
lst[1]='mysql'
print('修改数据之后：',lst,id(lst))
print('---------------------')
```



#### 列表排序

```python 
lst=[4,56,3,78,40,56,89]
print('原列表：',lst)

lst.sort()
print('升序后：',lst)

lst.sort(reverse=True)
print('降序后：',lst)

print('-'*30)

lst2=['banana','apple','orange','tomato','allow','Xcom','Cat','Dog']
print('原列表：',lst2)

lst2.sort()
print('升序后：',lst2) # 先排大写

lst2.sort(reverse=True)
print('降序后：',lst2)

# 忽略大小写=统一大小写
import sys
print(sys.version)
lst2.sort(key=lambda x: x.lower())
print('忽略大小写后：',lst2)


#################
lst=[4,56,3,78,40,56,89]
print('原数字列表：',lst)
acs_lst=sorted(lst)
print('升序后列表：',acs_lst)
dcs_lst=sorted(lst,reverse=True)
print('降序后列表：',dcs_lst)
print('-'*40)
lst2=['banana','apple','orange','tomato','allow','Xcom','Cat','Dog']
print('原字符串列表：',lst2)
acs_lst2=sorted(lst2)
print('升序后列表：',acs_lst2)
dcs_lst2=sorted(lst2,reverse=True)
print('降序后列表：',dcs_lst2)
mcs_lst2=sorted(lst2,key=lambda x: x.lower())
print('忽略大小写后列表：',mcs_lst2)
```





 #### 列表生成式

```shell 
import random

lst=[item for item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)

lst=[random.randint(1,100) for _ in range(10)]
print(lst)

lst=[i for i in range(10) if i%2==0]
print(lst)
```



#### 二维列表

```shell
lst=[
    ['城市','环比','同比','定基'],
    ['北京','103.4','129.8','122.5'],
    ['上海','103.5','120.8','123.5'],
    ['广州','102.1','144.3','105.5'],
]
print(lst)

for row in lst:
    for item in row:
        print(item,end='\t')
    print()

lst2=[ [j for j in range(5)] for i in range(4)]
print(lst2)
```





### 1.33 元组

```python 
t=('hello',[10,20,30],'python','world')
print(t)

t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

print('10在元组中是否存在：',(10 in t))
print('10在元组是不存在：',(10 not in t))
print('最大值：',max(t))
print('最小值：',min(t))
print('len:',len(t))
print('t.count:',t.count(10))
print('t.index:',t.index(10))

y=(10,)
print(y,type(y))

u=10
print(u,type(u))

del t
# print(t)# NameError: name 't' is not defined
```



#### 元组生成式

```python
t=(i for i in range(4))
print(t)

# t=tuple(t)
# print(t)

# for item in t:
#     print(item)

print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())

t=tuple(t)
print(t)
```





### 1.34 字典

```python
d={10:'cat',20:'dog',30:'pet',40:'zoo'}
print(d)

lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
ZipObj=zip(lst1,lst2)
print(ZipObj)
d=dict(ZipObj)
print(d)

d=dict(cat=10,dog=20)
print(d)
print('max', max(d))
print('min', min(d))
print('len', len(d))

del d
# print(d)

t=(10,20,30)
print({t:10})

# lst=[10,20,30]
# print({lst:10}) # TypeError: unhashable type: 'list'
```



#### 字典访问与遍历

```python
d={'hello':10 , 'world':20 , 'python':30}
print(d['hello'])
print(d.get('hello'))

# print(d[java]) # NameError: name 'java' is not defined
print(d.get('java'))
print(d.get('java','不存在'))

for item in d.items():
    print(item)

for key,value in d.items():
    print(key,'--->',value)
```





#### 字典操作方法

```python
d={1001:'李梅',1002:'张展',1003:'华生'}
print(d)

d[1004]='张丽丽'
print(d)

keys=d.keys()
print(keys)

print(list(keys))
print(tuple(keys))

values=d.values()
print(values)
print(list(values))
print(tuple(values))

lst=list(d.items())
print(lst)
s1=tuple(d.items())
print(s1)

d=dict(lst)
print(d)
# d=dict(s1)
# print(d)


print(d.pop(1001))
print(d.pop(2009,'None'))
print("--删除之前--")
print(d)
print((d.popitem()))
print("--删除之后--")
print(d)

print(bool(d))
d.clear()
print(d)

print(bool(d))
```



#### 字典生成式

```python 
import random
d={item: random.randint(1,100) for item in range(4)}
print(d)

lst=[1001,1002,1003]
lst2=['陈美娜','王康建','左秋兰']
d={key:value for key,value in zip(lst,lst2)}
print(d)
```



### 1.35 集合

```python
s={10,20,30,40}
print(s,type(s))

# s={[10,20],[30,40]}
# print(s) # TypeError: unhashable type: 'list'

s=set()
print(s,type(s),bool(s))

s={}
print(s,type(s))

s=set('helloworld')
print(s)

s2=set([10,20,30])
print(s2)
s3=set(range(1,10))
print(s3)
print('max:',max(s3))
print('min:',min(s3))
print('len:',len(s3))

print('9在集合中存在吗？',(9 in s3))
print('9不存在集合中吗？',(9 not in s3))
del s3
# print(s3) #NameError: name 's3' is not defined. Did you mean: 's'?
```



#### 集合操作符

```python
A={10,20,30,40,50}
B={30,50,88,75,20}

print('并集',A|B)
print('交集',A&B)
print('差集',A-B)
print('补集',A^B)
```



#### 集合相关操作

```python
s={10,20,30}
s.add(199)
print(s)
s.remove(20)
print(s)
# s.clear()
# print(s)
for item in s:
    print(item)
for index,item in enumerate(s):
    print(index,'---->',item)
for index,item in enumerate(s,start=10):
    print(index,'---->',item)
s={i for i in range(1,10)}
print(s)
s={i for i in range(1,10) if i%2==1}
print(s)
```



#### python3.11 新特性

```PYTHON
# 同步迭代
# fruits={'apple','orange','pear','grape'} # 集合是无序的
fruits=['apple','orange','pear','grape']
counts=[10,3,5,8]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('10个苹果')
        case 'orange',3:
            print('3个橘子')
        case 'pear',5:
            print('5个梨子')
        case 'grape',8:
            print('8个葡萄')
# 集合合并
d1={'a':10,'b':20}
d2={'c':30,'d':40,'e':50}
merged_dict=d1|d2
print(merged_dict)
```





#### 实战1: 千年虫

```python
lst=[88,89,90,00,90]
print(lst)
print('200'+str(00)) # 00 字符串之后会变0

# for index in range(len(lst)):
#     if str(lst[index])!='0':
#         lst[index]='19'+str(lst[index])
#     else:
#         lst[index]='200'+str(lst[index])
# print('修改后的年份列表：',lst)

for index,value in enumerate(lst):
    print(index,'--->',value)

for index,value in enumerate(lst):
    if str(value)!='0':  # 注意单引号
        lst[index]='19'+str(value)
    else:
        lst[index]='200'+str(value)
print('修改后的年份列表：',lst)
```



#### 实战2：购物车

```PYTHON
lst=[]  # 空列表，相当于空库房
for i in range(5): # 模拟需求，让用户操作5次
    goods=input('请输入商品的四位数编号和商品名称进行入库操作，每次只允许一件商品：') # 接收用户输入
    lst.append(goods) # 追加到列表，添加到购物车

for item in lst: # 循环展示列表中所有元素，库房中所有商品都展示出来
    print(item)
print(lst)

wares=[] # 空列表，用于存储购物车中的商品
while True:
    flag=False # 当前购物车中还没有商品的情况，默认值为False
    num=input('请输入要购买的商品编号：')  # 输入商品编号
    for item in lst: # 遍历下库房列表，查看所有元素
        if num==item[0:4]: # 截取元素的首四位，即数字编号
            flag=True # 设置当前购物车状态
            wares.append(item) # 添加商品编号到购物车
            print(num,'已成功添加到购物车')
            break # 退出当前if判断
    if not flag and num!='q':
        print('商品不存在')
    if num=='q':
        break

print('-'*50)
print('您购物车里已选的商品为：')
wares.reverse()
for item in wares:
    print(item)
```



#### 实战3：12306买票

```python
# 车次字典
dict_ticket={
    'G1568': ['北京南-天津南','18:06','18:39','00:33'],
    'G1567': ['北京南-天津南','18:15','18:49','00:35'],
    'G8917': ['北京南-天津西','18:20','18:19','00:59'],
    'G2029': ['北京南-天津南','18:35','19:08','00:35']
}

print('车次   出发站-到达站      出发时间      到达时间     历时时长')

# 遍历
for key in dict_ticket:
    print(key,end=' ') # 不换行，因为车次和其他信息在同一行展示
    for item in dict_ticket.get(key): # 根据键获得值
        print(item,end='\t\t')
    print()

train_num=input('请输入要购买的车次：')
info=dict_ticket.get(train_num,'车次不存在')
if info!='车次不存在':
    person=input('请输入乘车人，多人请使用逗号分隔：')
    s=info[0] +' '+info[1]+'开'
    print('您已购买了'+train_num+' '+s+',请'+person+'尽快换取纸质车票。【12306铁路客服】')
else:
    print('对不起，您选择的车票可能不存在')
```



#### 实战4：通讯录

```python
# 创建空集合
s=set()
# 设置循环次数
for i in range(1,6):
    info=input(f'请输入第{i}位好有的手机号：')
    s.add(info)
# 遍历集合
for item in s:
    print(item)
```



### 1.36 字符串

#### 字符串操作1

```python
s='HelloWorld'
# 字符串的替换
net_s=s.replace('o','你好',1)
print(net_s)

# 字符串在指定的宽度范围内居中
print(s)
print(s.center(20))
print(s.center(20,'*'))

s='    Hello    World  '
print(s.strip()) # 去除字符串左右的空格
print(s.lstrip()) # 去除字符串左侧空格
print(s.rstrip()) # 去除右侧空格

s3='dl-Helloworld'
print(s3.strip('ld'))  # 去除指定字符串,与顺序无关
print(s3.lstrip('ld')) # 去除左侧指定字符串
print(s3.rstrip('ld')) # 去除右侧指定字符串
```



#### 字符串操作2

```python
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
```





#### 字符串的格式化操作

```python
age=18
name='马冬梅'
score=98.5
# 通过占位符进行格式化
print('姓名：%s,年龄：%d,成绩：%.1f' % (name,age,score))
print('姓名：%s,年龄：%d,成绩：%f' % (name,age,score))
# 通过f-string进行格式化
print(f'姓名：{name},年龄：{age},成绩：{score}')
# 通过字符串的format方法
print('姓名：{0},年龄：{1}，成绩：{2}'.format(name,age,score)) # 0,1,2 对应format 中的参数顺序
print('姓名：{2},年龄：{1}，成绩：{0}'.format(score,age,name))
```





#### 字符串format详细格式控制

```python
s='helloworld'
print('{0:*<20}'.format(s)) #0,format起始位 : 引导符号 *填充符号，只能是单个 <左对齐>右对齐^居中对齐 20 长度
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))
print(s.center(20,'*')) # 居中对齐

print('{0:.2f}'.format(312345552323.23)) # 保留2位小数
print('{0:.4}'.format('312345552323')) #保留4位整数

a=242 # 整数类型
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x},十六进制:{0:X}'.format(a))

b=3.1415926 # 浮点类型
print('{0:.2f},{0:.2E},{0:2e},{0:.2%}'.format(b))
```





#### 字符串的编码与解码

```python
s='伟大的中国梦'
ucode=s.encode(errors='replace')  # utf8 18个字节长度，1中文在gbk中占3个字节
print(ucode)

gcode=s.encode(encoding='gbk',errors='replace') # gbk 12个字节长度，1中文在gbk中占2个字节
print(gcode)

s2='耶✌'
# ecode=s2.encode(encoding='gbk',errors='strict') #  can't encode character '\u270c'  #无法编码就报错
# ecode=s2.encode(encoding='gbk',errors='ignore') # 自动忽略无法编码的问题
ecode=s2.encode(encoding='gbk',errors='replace') # 自动替换无法编码的字节为问号
print(ecode)

dcode=bytes.decode(gcode,encoding='gbk') # 解码所用类型要与编码一致
print(dcode)
d2code=bytes.decode(ucode,encoding='utf-8')
print(d2code)
d3code=bytes.decode(ucode,encoding='gbk') # 不一致就乱码
print(d3code)
```





























