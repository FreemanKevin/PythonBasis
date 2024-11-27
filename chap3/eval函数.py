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
# print(eval(hello)) # NameError: name '北京欢迎您' is not defined
