class Person:
    name = "张三"
    age = 18

    def hello(self):
        """
            1.在方法中不能直接访问，类中属性
            2.每次调用都会默认传递一个实参，必须显示指定否则：
                TypeError: eat() takes 0 positional arguments but 1 was given
            3.类方法中的第一个参数，默认是会传入当前对象
            参数
                self:当前对象本身，默认传入；相当java中的this
        """
        print("id=%s,你好~ 我是:%s"%(id(self),self.name))

p1 = Person()
print(p1.name,p1.age)   
print("p1Id=",id(p1))
# 调用方法 对象名.方法名()
p1.hello()
