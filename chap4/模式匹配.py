score=input('请输入成绩：')
match score:  # python3.11+ 新特性
    case 'A':
        print('优秀')
    case 'B':
        print('及格')
    case 'C':
        print('勉强')
    case 'D':
        print('未通过')