# 序列是 python 中的基本数据结构的一种
# 序列分类：
#   可变序列：
#        > 列表（list）
#   不可变序列：
#        > 字符串（str）
#        > 元组 （tuple）

username = "张师傅"
print(username[:2])


# list修改
usernames = ["张三","李四","王五","赵六"]
print("修改前",username)

usernames[0]="zhangs"
print("修改后",usernames)

# 切片赋值

# usernames[:2] = 123
# 切片修改必须使用对应序列进行赋值,如果赋值元素个数大于匹配个数则插入元素
usernames[:2] = ["zs","lis"]
print("切片修改",usernames)

# 设置切片后修改赋值，值元素个数必须跟切片数匹配

usernames[::2] = ["a","b"]
print("切片修改步长",usernames)

# 删除列表元素
del usernames[0]
print("删除第一个元素",usernames)


# 通过切片删除
del usernames[:1]
print("切片删除",usernames)


# 修改操作只能是可变序列

s = "hello"
# s[0] = "H"
# 如果要改变则需要将其转为可变序列
ss = list(s)
print(ss)


