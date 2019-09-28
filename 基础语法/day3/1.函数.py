# 函数
# 函数介绍
#   - 函数也是一个对象
#   - 对象是内存中专门存储数据的一块区域
#   - 函数可以用来保存可执行的代码
#   - 函数将一连串的相关性功能代码 封装 达到可重用
# 语法
# def 函数名([形参1,形参2....]) :
#   代码块

# 定义函数
def firstFun() :
    print("这是我的第一个python函数")

# 查看类型
print(type(firstFun))

# 调用函数
firstFun()    


# 带参数返回值的函数
def sum(one,two):
    return one+two

print(sum(1,1))

# 带默认值的参数
def sum2(one = 0,two = 0):
    return one + two

print(sum2(),sum2(1),sum(1,2))

# 关键字参数：可以不用根据参数位置传递参数 根据 参数名称传递参数
# 位置参数可以跟关键字参数混合使用
# 混合使用：位置参数必须在前面，不可出现在后面及重复使用关键字参数赋值
print(sum2(two=5),sum2(10,two=5))


# 不定长度参数
# 在参数前添加一个 * 号，所有的参数会被保存到一个元组中
# 一个函数中参数列表只允许有一个 带 * 参数，可出现在任何位置但是在 * 参数后面必须使用 关键字方式传参
def sum3(*numbers):
    sum = 0
    for item in numbers:
       sum += item
    return sum

print(sum3(1,2,3))

# 了个 ** 作为参数，必须使用键值对的方式传递
# 一个函数中只能存在一个 ** 参数，改参数可以和形参配置使用，只能放在函数末尾
def printStr(**strs):
    print(strs)

printStr(name="张三",age=18)


# 参数解包
def fun(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

# 解包格式得和参数数量一致
a = (1,2,3,5,6)
fun(*a[:3])    

# 解包字典,必须跟参数名称对应
b = {"a":11,"b":22,"c":33}
fun(**b)  


# 添加函数参数及返回值描述
def commentFun(a:int,b:bool) -> int:
    return a if b else 0

print("commentFun=",commentFun(1,0))

# 编写函数帮助描述
def myFun() :
    '''文档描述字符串
       主要是学习用的
       会打印一句myFun
    '''
    print("myFun")

# 获取帮助函数
help(print)
help(myFun)

