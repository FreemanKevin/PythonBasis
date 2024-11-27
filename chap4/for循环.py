
for i in "hello":
    print(i)

for i in range(1,11):
    print(i)

s=0
for i in range(1,11):
    s+=i
print(s)

"""
153=5**3+3**3+1**3
"""
for i in range(100,1000):
    gn=i%10
    sn=i//10%10
    bn=i//100
    if i==gn**3+sn**3+bn**3:
        print(i)
