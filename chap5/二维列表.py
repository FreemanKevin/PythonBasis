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
