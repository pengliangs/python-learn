# 面向对象（OOP）
# python 是一门面向对象的编程语言
# 语法：class 类名():
class MyClass():
    pass

print(MyClass,type(MyClass))
# 创建对象就像调用函数一样
my_class = MyClass()
print(type(my_class),my_class)

# isinstance 检查一个对象是否是一个类的示例
print(isinstance(my_class,MyClass))
print(isinstance(my_class,str))

# 使用类创建对象简化流程
# class MyClass:    id=0x123,type=<class 'type'>
#     pass
# mc = MyClass      id=0x456,type=MyClass
# 1.创建一个变量mc
# 2.在内存中创建一个新对象
# 3.将对象的id赋值给变量

# 在对象中添加一个属性
my_class2 = MyClass()
my_class2.name = "张三"
print(my_class2.name)
