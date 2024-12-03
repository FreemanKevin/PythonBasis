lst=[]  # 空列表，相当于空库房
for i in range(5): # 模拟需求，让用户操作5次
    goods=input('请输入商品的四位数编号和商品名称进行入库操作，每次只允许一件商品：') # 接收用户输入
    lst.append(goods) # 追加到列表，添加到购物车

for item in lst: # 循环展示列表中所有元素，库房中所有商品都展示出来
    print(item)
print(lst)

wares=[] # 空列表，用于存储购物车中的商品
while True:
    flag=False # 当前购物车中还没有商品的情况，默认值为False
    num=input('请输入要购买的商品编号：')  # 输入商品编号
    for item in lst: # 遍历下库房列表，查看所有元素
        if num==item[0:4]: # 截取元素的首四位，即数字编号
            flag=True # 设置当前购物车状态
            wares.append(item) # 添加商品编号到购物车
            print(num,'已成功添加到购物车')
            break # 退出当前if判断
    if not flag and num!='q':
        print('商品不存在')
    if num=='q':
        break

print('-'*50)
print('您购物车里已选的商品为：')
wares.reverse()
for item in wares:
    print(item)




