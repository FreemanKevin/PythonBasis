import pyfiglet

def print_alibaba_logo():
    """打印一个花里胡哨的阿里巴巴Logo"""
    result = pyfiglet.figlet_format("GuoDi", font="slant")  # 这里可以更换字体
    print(result)

print_alibaba_logo()