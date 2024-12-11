s='伟大的中国梦'
ucode=s.encode(errors='replace')  # utf8 18个字节长度，1中文在gbk中占3个字节
print(ucode)

gcode=s.encode(encoding='gbk',errors='replace') # gbk 12个字节长度，1中文在gbk中占2个字节
print(gcode)

s2='耶✌'
# ecode=s2.encode(encoding='gbk',errors='strict') #  can't encode character '\u270c'  #无法编码就报错
# ecode=s2.encode(encoding='gbk',errors='ignore') # 自动忽略无法编码的问题
ecode=s2.encode(encoding='gbk',errors='replace') # 自动替换无法编码的字节为问号
print(ecode)

dcode=bytes.decode(gcode,encoding='gbk') # 解码所用类型要与编码一致
print(dcode)
d2code=bytes.decode(ucode,encoding='utf-8')
print(d2code)
d3code=bytes.decode(ucode,encoding='gbk') # 不一致就乱码
print(d3code)
