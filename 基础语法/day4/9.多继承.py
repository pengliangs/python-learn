class A :
    def test(self):
        print("test-A")

    def test1(self):
        print("A")

class B :
    def test(self):
        print("test-B")

    def test2(self):
        print("B")

# 多继承
class C(A,B) :
  pass

# 类名.__bases__ 属性可以用来获取当前类的所有父类
print(C.__bases__)

c = C()
# 如果多继承中存在相同方法，会先找当前类是否存在然后根据继承列表顺序找
c.test()
c.test1()
c.test2()

# 在实际开发中不推荐使用多继承，会导致程序的复杂度上升