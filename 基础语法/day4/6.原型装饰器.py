
class Dog:
    def __init__(self,name):
        self._name = name

    # 每一次回去值都要调用一下方法，提麻烦的
    # 这个时候可以通过,系统内置的装饰器 @property 将getter方法装饰为一个属性值
    @property
    def name(self):
        return self._name
        
    # setter方法装饰器：@属性名.setter
    # 使用setter装饰器，必须要有getter装饰器
    @name.setter    
    def name(self,name):
        self._name = name

    def hello(self):
        print("你好，我是:%s"%self._name)

d = Dog("旺财")

d.name = "大黄"
d.hello()