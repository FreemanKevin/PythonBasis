# fruits={'apple','orange','pear','grape'}
fruits=['apple','orange','pear','grape']
counts=[10,3,5,8]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('10个苹果')
        case 'orange',3:
            print('3个橘子')
        case 'pear',5:
            print('5个梨子')
        case 'grape',8:
            print('8个葡萄')
