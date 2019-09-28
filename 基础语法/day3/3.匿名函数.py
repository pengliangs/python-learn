# 匿名表达式 lambda函数表达式
# 语法: lambda 参数列表:返回值
# 匿名函数一般都是作为参数使用
numbers = [1,10,9,7,23,6,132]

res = list(filter(lambda num: num >100,numbers))
print(res)

res = list(map(lambda i: i+1,numbers))
print(res)

strs = ["admin","accp","username","up"]
strs.sort(key=len)
print(strs)

# sorted 跟stort一样，但是可以操作任意序列；不会影响原序列
number_str = "123432412312312334654645"
print(sorted(number_str),number_str)


number_strs = [1,"4","6","2",56,21]
print(sorted(number_strs,key=int))