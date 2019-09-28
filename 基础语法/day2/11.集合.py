# 集合（set）
# 集合和列表相似
# 不同点
#   > 集合中只能存储不可变对象
#   > 集合中存储的对象是无序的
#   > 集合中不能出现重复的元素

# 创建集合
s = {1,2,3,4,5,1,2,3,4,5}
print(s,type(s))

# 创建一个空集合
s = set()

# 列表转换集合
s = set([1,2,3,4,5,6,1,2,3])
print(s)

# 字符串转集合
s = set("hello")
print(s)

# 字典转集合,只会包含键
s = set({"name":"张三","age":18})
print(s)

# 集合不能通过索引操作
# print(s[0])

# 添加元素
s = {1,2,3}
s.add(4)
s.add(5)
s.add(5)
print(s)

# 将一个集合中的元素添加到集合中
s = {1,2,3}
ss = {1,2,3,4,5,6}
s.update(ss)
print(s)


# 随机删除集合元素
s = {1,2,3,4,5,6}
print(s.pop())


# 删除集合中元素
s = {1,2,3,4,5,6}
s.remove(1)
s.remove(6)
print(s)

# 清空集合
s.clear()
print(s)

# 浅拷贝
s = {1,2,3,4,5,6}
b = s.copy()
s.add(7)
b.add(8)
print(s)
print(b)