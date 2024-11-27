number=eval(input('请输入你的数字：'))
if number==123456:
    print('中奖')
else:
    print("谢谢惠顾")

# 使用条件表达式简化
print('中奖') if number==123456 else print('谢谢惠顾')

