s=0
i=1
while i<=100:
    if i%2==1:
        i+=1
        continue
    s+=i
    i+=1
print("一百以内的偶数之和：",s)
#
s=0
i=1
for i in range(1,101):
    if i % 2 == 1:
        i += 1
        continue
    s += i
print("一百以内的偶数之和：", s)