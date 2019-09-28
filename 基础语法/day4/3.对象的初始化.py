class Person:

    # 在类中可以定义一些特殊方法（魔术方法）
    # 特殊方法都是__开头，__结尾的方法
    # 特殊方法不需要我们自己调用，不要自己去尝试调用外部是可以调用到的
    # __init__ 有点像java中的构造函数，在对象创建的时候被调用

    # 创建对象流程
    # p1 = Person()
    # 1.创建一个变量
    # 2.在内存中创建一个新对象
    # 3.__init__(self) 方法执行
    # 4.将对象的id赋值给变量
    def __init__(self,name):
        # 初始化一个属性
        #self.name = ""
        self.name = name
        print("Person.__init__执行")

    def hello(self):
        print("你好~ 我是:%s"%self.name)

    print("Person中代码块，执行")

# p1 = Person()
# p1.name = "p1"
# p1.hello()

p2 = Person("p2")
p2.hello()