def sum(a , b):
    """
        求两数相加之和
    """
    return a + b

def nul(a , b):
    """
        求两数相乘的积
    """
    return a * b

# 在不修改原函数的情况下，在以上两个函数执行的时候进行前后打印，计算开始、计算结束语句
# 通过装饰器模式，可以在不修改源代码的情况下对代码进行扩展增强
def aspectAurround(fun):
    def aurround(*args , **kwarags):
        print("计算开始...")
        res = fun(*args , **kwarags)
        print("计算结束...")
        return res
    return aurround 



print("结果:",aspectAurround(sum)(a=1,b=2))
print("结果:",aspectAurround(sum)(2,2))


# python提供的装饰器使用
# 一个函数可以使用多个装饰器装饰，有点像java中的注解
# 多个装饰修饰执行顺序，从下往上
@aspectAurround
def fun():
    print("fun~~~~")

fun()    