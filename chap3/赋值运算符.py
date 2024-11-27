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


