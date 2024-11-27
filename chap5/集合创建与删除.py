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
