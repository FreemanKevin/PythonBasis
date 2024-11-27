score=eval(input("请输入您的成绩："))
if score <0 or score >100:
    print("输入有误")
elif score == 100:
    print("满分")
elif 60 <= score <100:
    print("通过")
else:
    print("未通过")

