# 列表 (list)
# 有点像javaScript中的集合使用方式
my_list = []
print(type(my_list))

my_list.append("1")
print(my_list)

my_list = [1,"hello",3,True,None]
print(my_list)
print("索引下1下的元素:",my_list[1])
for item in my_list:
    print("列表元素:",item)


# 切片
# 从现有列表中获取，一个子列表
usernames = ["张三","李四","王五","赵六"]

#python中可以使用负数，从后取值
print("usernames集合中last元素：",usernames[-1])

# 通过切片获取指定的元素
# 语法: 列表[起始位置:结束位置]
# 切片不会影响愿列表，返回新的列表
print(usernames[0:2])
print(usernames[0:])
print(usernames[:2])
print(usernames[2:2])
print(usernames[3:2])
print(usernames[0:-2])
print(usernames[:-1])
# 语法: 列表[起始位置:结束位置:跳跃步长]
# 步长可以是 负数 但是 不能为 0
print(usernames[::2])


# 通用操作
# + 号可以将两个数组追加合并为一个数组
my_list = [1,2,3] + [4,5,6]
print(my_list)

# * 可以将列表重复指定次数
my_list = [1,2,3] * 5
print(my_list)

# in 和 not in
# in：检查元素是否存在列表中
# not in：检查元素不存在列表中
usernames = ["张三","李四","王五","赵六","李四"]
print("张三" in usernames)
print("扎扎" in usernames)
print(2 in usernames)
print(2 not in usernames)
print("列表长度:",len(usernames))
print("列表最大值:",max(my_list))
print("字符最大值:",max("12345678910"))
# 没有的元素会抛异常,index第二个参数从第几个位置开始，第三个参数结束位置
print("李四在列表中索引:",usernames.index("李四"))
print("李四在列表中出现次数:",usernames.count("李四"))