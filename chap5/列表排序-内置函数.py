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