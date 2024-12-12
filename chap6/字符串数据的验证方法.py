# isdigit() 只能识别阿拉伯数字
print('123'.isdigit()) # True
print('一二三'.isdigit()) # False
print('0b1010'.isdigit()) # False
print('ⅠⅡⅢ'.isdigit()) # False
print('零壹贰'.isdigit()) # False
print('-'*20)

# isnumeric() 能识别阿拉伯数字、中文数字、繁体中文数字、罗马数字
print('123'.isnumeric()) # True
print('一二三'.isnumeric()) # True
print('0b1010'.isnumeric()) # False
print('ⅠⅡⅢ'.isnumeric()) # True
print('零壹贰'.isnumeric()) # True
print('-'*20)

# isalpha() 能识别字母，中文，繁体中文
print('helloworld123'.isalpha()) # False
print('helloworld一二三'.isalpha()) # True
print('helloworld0b1010'.isalpha()) # False
print('helloworldⅠⅡⅢ'.isalpha()) # False
print('helloworld零壹贰'.isalpha()) # True
print('-'*20)

# isalnum() 能识别数字，字母，中文，繁体中文
print('helloworld123'.isalnum()) # False
print('helloworld一二三'.isalnum()) # True
print('helloworld0b1010'.isalnum()) # False
print('helloworldⅠⅡⅢ'.isalnum()) # False
print('helloworld零壹贰'.isalnum()) # True
print('-'*20)


# islower() 判断字符的大小写
print('Hello'.islower())  # False
print('helloWorld'.islower()) # False
print('helloworld'.islower())  # True
print('hello你好'.islower()) # True # 默认中文既是大写，也可以是小写
print('-'*20)

# isupper() 判断字符的大小写
print('Hello'.isupper())  # False
print('HELLO'.isupper())  # True
print('HELLO你好'.isupper())  # True
print('HELLOWORLD'.isupper())  # True
print('helloWorld'.isupper()) # False
print('HelloWorld'.isupper())  # False
print('Hello你好'.isupper()) # False # 默认中文既是大写，也可以是小写
print('-'*20)

# istitle() 判断字符串的首字母大写
print('Hello'.istitle())  # True
print('HELLO'.istitle())  # False
print('HELLO你好'.istitle())  # False
print('HELLOWORLD'.istitle())  # False
print('helloWorld'.istitle()) # False
print('Hello World'.istitle())  # True
print('Hello world'.istitle())  # False
print('HelloWorld'.istitle())  # False
print('Hello你好'.istitle()) # True # 默认中文既是大写，也可以是小写
print('-'*20)


# isspace() 判断字符串是否是空字符
print(''.isspace())  # False
print(' '.isspace())  # True
print('\t'.isspace()) # True
print('\n'.isspace()) # True
print('-'*20)