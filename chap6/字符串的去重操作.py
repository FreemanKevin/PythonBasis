s='helloworldheloowoorldlllllooooooddddddrrrrw'
# 方法1：字符串拼接+not in
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item
print(new_s)

# 方法2：使用索引+not in
