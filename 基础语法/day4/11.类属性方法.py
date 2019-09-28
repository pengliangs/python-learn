class A:
    # 类属性，直接在类中定义的属性是类属性
    # 类属性可以通过类或类的示例访问
    #   > 类属性只能通过类对象来修改，无法通过实例对象修改
    count = 0
    def __init__(slef):
        # 实例属性
        # 实例属性只能通过实例修改，无法通过对象修改
        slef.name = ""

    # 实例方法
    #   > 在类中定义，已self为第一个参数的方法都是实例方法
    #   > 实例方法可以通过实例和类去调用
    #       > 实例调用，会自动注入当前对象为第一个参数self
    #       > 类调用，不会自动注入第一个参数
    def test(slef):
        print("test",slef)

    # 类方法
    # 在类内部使用 @classmethod 来修改的方法属于类方法
    # TypeError: test2() takes 0 positional arguments but 1 was given
    # 类方法的第一个参数是cls，也是自动注入，cls是当前类对象
    # 类方法可以通过对象调用也可以通过实例调用
    @classmethod
    def test2(cls):
        print("test2,这是一个类方法",cls)

    # 静态方法
    # 在类中使用 @staticmethod 来修饰的方法属于静态方法
    # 静态方法不会注入任何默认参数，静态方法可以通过类和实例调用
    # 静态方法：基本是一个和当前类无关的方法，他只是保存当前类的函数
    # 静态方法一般都是攻击类方法 
    @staticmethod
    def test3():
        print("test3,这是一个静态方法")    

a = A()
# 实例属性
a.count = 10
print("a=",a.count)
print("A=",A.count)    
a.test()
# A.test() TypeError: test() missing 1 required positional argument: 'slef'
A.test(a)

a.test2()
A.test2()

a.test3()
A.test3()