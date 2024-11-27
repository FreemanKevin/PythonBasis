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
