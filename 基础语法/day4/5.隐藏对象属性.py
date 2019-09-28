
class Dog:
    def __init__(self,name):
      
        # 可以为对象的属性使用刷下划线开通 __xxx
        # 双下划线开头的属性，是对象的隐藏属性，隐藏属性只能在类的内部访问，无法通过对象名访问
        # 其实隐藏属性只不过是python自动为属性改了一个名字
        #   实际上是将名字修改为了，_类名__属性名 
        #   如：_Dog__name
        self.__name = name

    def get_name(self):
        return self.__name
        
    def set_name(self,name):
        self.__name = name

    def hello(self):
        print("你好，我是:%s"%self.__name)

d = Dog("旺财")
d.__name = "小黑"
d.hello()

d._Dog__name = "大黄"
d.hello()


# 使用 __ 开头的属性，实际上依然可以在外部使用，所有这种方式我们一般不用
# 一般我们会将私有属性以一个下划线_开头
# 因为两个下划线是私有属性但是是假私有，反而还增加了复杂度，还不如写一个 
# 使用_开头一般都是私有属性，没有特殊需要不要直接修改

