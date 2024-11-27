t=(i for i in range(4))
print(t)

# t=tuple(t)
# print(t)

# for item in t:
#     print(item)

print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())

t=tuple(t)
print(t)
