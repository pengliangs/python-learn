# 特殊方法，也称为魔术方法
# 特殊方法是以__开头结尾
# 特殊方法一般不需要我们手动调用
# 官方文档: https://docs.python.org/zh-cn/3/reference/datamodel.html#basic-customization

class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    # 尝试将对象转换字符串的时候调用
    def __str__(self):
        return "Person[name=%s,age=%s]"%(self._name,self._age) 

    # 对当前对象使用repr函数时调用
    # 它的作用是指定对象在 “交互模式” 中直接输出的效果
    def __repr__(self):
        return "hello"

    # 对象是不可以直接使用 比较 运算符，如果要使用就得定义如下特殊函数    
     #__lt__(self, other)
     #__le__(self, other)
     #__eq__(self, other)
     #__ne__(self, other)
     #__gt__(self, other)
     #__ge__(self, other)

    # 在做大于比较的时候调用
    # self当前对象，other表示当前比较对象
    def __gt__(self, other):
        return self._age > other._age

    # 在 bool 转换的时候调用
    def __bool__(self):
        return self._age > 18
    # 模拟数字类型函数
    # __add__(self, other)
    # __sub__(self, other)
    # __mul__(self, other)
    # __matmul__(self, other)
    # __truediv__(self, other)
    # __floordiv__(self, other)
    # __mod__(self, other)
    # __divmod__(self, other)
    # __pow__(self, other[, modulo])
    # __lshift__(self, other)
    # __rshift__(self, other)
    # __and__(self, other)
    # __xor__(self, other)
    # __or__(self, other)
p1 = Person("张三",18)
p2 = Person("李四",28)
# <__main__.Person object at 0x002EFDD0>
# 在大于对象是，实际上打印的是对象中的特殊方法__str__()的返回值
print(p1)
print(repr(p1))
print(p1 > p2)

print(bool(p1),bool(p2))
