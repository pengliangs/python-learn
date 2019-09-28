class Animal:
    def run(slef):
        print("动物会跑~~~")

    def sleep(slef):
        print("动物会睡觉~~~")    

class Dog(Animal):
    def bark(slef):
        print("汪汪汪~~~")

    # Override
    def run(slef):
        print("狗会跑~~~")

# 如果在子类中有同名的方法，则通过子类实例去调用方法是当前子类的；会覆盖父类方法(Override)
d = Dog()
print(type(d))
d.run()
print(isinstance(d,Animal))
