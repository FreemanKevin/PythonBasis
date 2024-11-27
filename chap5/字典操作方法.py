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



