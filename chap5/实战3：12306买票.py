# 车次字典
dict_ticket={
    'G1568': ['北京南-天津南','18:06','18:39','00:33'],
    'G1567': ['北京南-天津南','18:15','18:49','00:35'],
    'G8917': ['北京南-天津西','18:20','18:19','00:59'],
    'G2029': ['北京南-天津南','18:35','19:08','00:35']
}

print('车次   出发站-到达站      出发时间      到达时间     历时时长')

# 遍历
for key in dict_ticket:
    print(key,end=' ') # 不换行，因为车次和其他信息在同一行展示
    for item in dict_ticket.get(key): # 根据键获得值
        print(item,end='\t\t')
    print()

train_num=input('请输入要购买的车次：')
info=dict_ticket.get(train_num,'车次不存在')
if info!='车次不存在':
    person=input('请输入乘车人，多人请使用逗号分隔：')
    s=info[0] +' '+info[1]+'开'
    print('您已购买了'+train_num+' '+s+',请'+person+'尽快换取纸质车票。【12306铁路客服】')
else:
    print('对不起，您选择的车票可能不存在')
