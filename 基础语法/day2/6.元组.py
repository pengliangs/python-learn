# 元组 tuple
# 元组是不可变序列
# 元组的操作方式基本和列表一样
# 使用()创建元组
my_tuple = ()
print(my_tuple,type(my_tuple))


my_tuple = (1,2,3)
print(my_tuple)


for item in my_tuple:
    print(item)

# 当元组不为空 可以省略 ()

my_tuple = 1,2,3,4,5,6
print(my_tuple,type(my_tuple))

# 如果元组不为空，最少要有一个逗号
my_tuple = (40)
print(my_tuple,type(my_tuple))


# 元组解包,需要跟元组个数对应
# 也可以在变量前添加一个 * 号接收剩余数量（只能存在一个*号，否则异常）
my_tuple = 1,2,3,4
a,b,c,d = my_tuple
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)

a,b,*c = my_tuple 
print(c)

# a,b值互换
a = 100
b = 300
print("交换前:a=",a,",b=",b)
a,b = b,a
print("交换后:a=",a,",b=",b)