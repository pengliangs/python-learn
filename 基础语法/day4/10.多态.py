class Animal:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
         self._name = name

    def hello(self):
        print("我是一只 %s"%self._name)

class Dog(Animal):

    def __len__(self):
        return 0

class Cat(Animal):
    pass

d = Dog("哈士奇")
c = Cat("加菲猫")
d.hello()
c.hello()

# 这个在python中是违反了多态，只用于处理一种指定类型的函数适应性比较差
def hello(animal):
    if isinstance(animal,Animal):
        print("这是一个多态函数,%s 进入"%animal.name) 

hello(d)    
hello(str())


# len()
# 之所以可已通过len() 来获取长度，是因为对象中具有一个特殊方法 __len__
# 也就是说只要对象中有 __len__ 特殊方法，就可以使用len()来获取长度
print(len(d))
# print(len(c)) 
