# 跟其他语言一样，就是引用类型和值类型
a = [1,2,3]
b = a
b[0] = 10
print(id(a),id(b))
print(a,b)

a = [1,2,3]
print(id(a))


# ==,!= 比较的是对象值是否相等
# is,is not 比较的是对象id是否相等
a = [1,2,3]
b = [1,2,3]
c = a
print(id(a),id(b))
print(a == b)
print(a is b)
print(a is c)
