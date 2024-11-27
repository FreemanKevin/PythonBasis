answer=input('请问您喝酒了吗？')
if answer=='y':
    proof=eval(input("请输入酒精含量："))
    if proof<=20:
        print("你可以开车")
    else:
        print("你不可以开车")
else:
    print("请开走，Goodbye!")