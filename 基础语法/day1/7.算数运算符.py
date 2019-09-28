# 算数运算符（+，-，*，/，%）
print("加",1 + 1)
print("减",2 - 1)
print("剩",2 * 2)
print("除",10 / 2)
print("模",10 % 2)
# 赋值运算符（=，+=，-=，*=，/=,%=）
# 比较运算符（>,>=,==,<,<=,!=）
print(2 > 1)
print(2 >= 3)
print(2 == 2)
print(2 < 3)
print(2 <= 3)
print(2 != 3)
print(2 > True)
# python中运逻辑运算符可以写一串
# 1 < 2 < 3 分为两部分看 1 < 2 and 2 < 3
print("python独有",1 < 2 < 3)
# 字符串可以进行比较，通过单个字符逐个比较Unicode编码比较
print('a' > 'b')
# 逻辑运算符（and 与、or 或、not 非）

True and print("骚气")
False and print("这个比较骚")

# 非布尔值的与或非运算
# python会将其当做布尔运算，最终返回原值

# 与运算：是找flase的值返回，如果第一个值是false直接返回，否则返回第二个值
print(1 and 2)
print(0 and 2)
print('' and 2)
print(None and 2)

# 或运算：是找true的值返回，如果第一个值为true直接返回，否则返回第二个值
print(0 or 1)
print(2 or 0)
print(None or 3)
print('' or 4)


# 条件运算符（三元运算符）
# 语法 语句1 if 条件表达式 else 语句2

print("好诡异的三元运算符") if True else print("咦")

# 运算符优先级，自己去看官方文档