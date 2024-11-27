d={'b':20}
d2=d
print(d2['b'])
d['b']=100 # 100 d={'b':100}
print(d['b'])
print(d2['b'])
print(d['b']+d2['b'])

lst=[1,3,5,7,9]
print(lst.reverse())

lst = [1, 3, 5, 7, 9]
reversed_lst = list(reversed(lst))  # 将reversed()返回的迭代器转换为列表
print(reversed_lst)
lst = [1, 3, 5, 7, 9]
reversed_lst = lst[::-1]  # 创建一个反转后的新列表
print(reversed_lst)