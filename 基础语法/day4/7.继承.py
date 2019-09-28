class Animal:
    def run(slef):
        print("动物会跑~~~")

    def sleep(slef):
        print("动物会睡觉~~~")    

# 在定义类是，可以在类名后括号中指定当前类的父类
class Dog(Animal):
    def bark(slef):
        print("汪汪汪~~~")

class Hashiqi(Dog):
    def cai_jia(slef):
        print("我是一只哈士奇，我最喜欢拆家了")

d = Dog()
print(type(d))
d.run()
d.sleep()
d.bark()
print(isinstance(d,Animal))

h = Hashiqi()
h.cai_jia()
h.bark()

# issubclass 检查类是否是另一个对象的子类
print(issubclass(Animal,object))
print(issubclass(Dog,Animal))
print(issubclass(Hashiqi,Animal))
print(issubclass(Animal,Dog))