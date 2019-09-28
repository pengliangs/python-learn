# 自定义异常
# 创建一个类 继承 Exception
class MyException(Exception):
    pass


def sum(a , b):
    if a < 0 or b < 0:
        # raise 用于向外部抛出异常，后面跟着一个异常类
        raise MyException("参数 a,b 不可出现负数")
    return a + b

print(sum(-1,2))