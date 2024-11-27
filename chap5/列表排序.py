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
