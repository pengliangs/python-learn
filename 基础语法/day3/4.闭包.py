# 闭包
# 跟javaScript中的几乎一样
# 就是函数中定义函数

# 返回内部函数
def fun():
    def fun2():
        print("内部函数fun2")
    return fun2

# 调用内部函数    
fun()()

def fun2():
    def fun3():
        print("内部函数fun3")
    fun3()
fun2()