class Animal:

    def __init__(self,name):
        self._name = name
        print("执行父类Animal")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
         self._name = name

    def run(slef):
        print("动物会跑~~~")

    def sleep(slef):
        print("动物会睡觉~~~")    

class Dog(Animal):

    def __init__(self,name,age):
        # 使用super调用父类的初始化方法
        super().__init__(name)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
         self._age = age

    def bark(slef):
        print(slef.name,"汪汪汪~~~")

    # Override
    def run(slef):
        print(slef.name,"狗会跑~~~")

# 如果在子类中有同名的方法，则通过子类实例去调用方法是当前子类的；会覆盖父类方法(Override)
d = Dog("狗子",1)
print(type(d))
d.run()
print(isinstance(d,Animal))
