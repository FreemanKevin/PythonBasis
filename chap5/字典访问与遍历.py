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