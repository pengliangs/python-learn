# 封装getter,setter方法
# 隐藏属性不希望外界直接访问，对外提供统一的getter,setter
# 增加对象安全性，合理的控制属性的只读方法
#   如果希望是只读的就去除 getter方法，如果不能被外界访问就去除 getter方法
# 在setter方法中可以做一些数据及类型的验证
class Dog:
    def __init__(self,name):
        # 不期望外界访问name属性，修改name名称hidden_name表示一个非外部访问属性，
        # 但是外部依然可以用到我们假装是不可访问
        self.hidden_name = name

    # getter方法
    def get_name(self):
        return self.hidden_name
    # setter方法
    def set_name(self,name):
        self.hidden_name = name

    def hello(self):
        print("你好，我是:%s"%self.hidden_name)

d = Dog("旺财")
d.set_name("小黑")
d.hello()
