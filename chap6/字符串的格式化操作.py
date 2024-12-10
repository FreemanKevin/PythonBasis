age=18
name='马冬梅'
score=98.5
# 通过占位符进行格式化
print('姓名：%s,年龄：%d,成绩：%.1f' % (name,age,score))
print('姓名：%s,年龄：%d,成绩：%f' % (name,age,score))
# 通过f-string进行格式化
print(f'姓名：{name},年龄：{age},成绩：{score}')
# 通过字符串的format方法
print('姓名：{0},年龄：{1}，成绩：{2}'.format(name,age,score)) # 0,1,2 对应format 中的参数顺序
print('姓名：{2},年龄：{1}，成绩：{0}'.format(score,age,name))
