# 字典 (dict)
# 键值对结构
print("----------------创建字典方式----------------")
user_info = dict(one=1,two=2,three=3) #dict创建的字典 所有 key都是字符串
print(user_info)
user_info = {}
print(type(user_info))
user_info = {"name":"张三","age":18}
print(user_info)

print("----------------将一个包含双值的子序列转换为字典----------------")
# 什么是双值序列？
# 序列中只包含两个值 如：[1,2],(1,2),'ab'
# 子序列：如果序列中的元素也是序列，那么我们就称这个元素为子序列
# [(1,2),(3,4)]
user_info = dict([("name","张三"),("age",28)])
print(user_info)

print("----------------获取序列长度----------------")
print(len(user_info))

print("----------------in和not in区别----------------")
# in 字典中包含指定的 key
# not in 字典中不包含指定的key
print("name" in user_info)
print("uname" in user_info)
print("uname" not in user_info)

print("----------------字典取值----------------")
# 取值，如果建不存在key会报错
print(user_info["name"])

# 取值，如果不存在返回None,也可以指定默认值
print(user_info.get("name"))
print(user_info.get("hello"))
print(user_info.get("hello","默认值"))

print("----------------修改字典值----------------")
# 修改字典
user_info["name"] = "大佬"
print(user_info)

# 如果key存在返回key,不存在向字典中添加 key并设置value
a = user_info.setdefault("name","设置key")
print(a,user_info)
a = user_info.setdefault("name3","设置key")
print(a,user_info)

print("----------------添加新值----------------")
user_info["hello"] = "xxx"
print(user_info)


print("----------------将其他字典值更新到当前字典----------------")
a = {"name":"张三","age":18}
b = {"name":"李四","age":28,"sex":"男"}
a.update(b)
print(a)
