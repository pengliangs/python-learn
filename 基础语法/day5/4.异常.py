try:
    # 可能出现错误的代码
    print(1/0)
    print("try")
except:
    # 出现错误的处理语句
    print("except")
else:
    # 没有出错时执行的语句    
    print("else")

print("---------------------------------------------------")

try:
    # 可能出现错误的代码
    print(2/1)
    print("try2")
except:
    # 出现错误的处理语句
    print("except2")
else:
    # 没有出错时执行的语句    
    print("else2")

print("---------------------------------------------------")

try:
    print(1/0)
except ZeroDivisionError as er:
    # except后面不加任何内容，则捕获的是所有异常
    # 如果在except后跟着一个异常类型那么它是会捕获该类型异常
    print("ZeroDivisionError",er)
except NameError as er:
    print("NameError",er)   
except:
    # 不写默认 Exception
    print("未知异常")    
finally:
    print("不管有没有异常，我都执行")    


print("---------------------------------------------------")

# 抛出异常
def sum(a , b):
    if a < 0 or b < 0:
        # raise 用于向外部抛出异常，后面跟着一个异常类
        raise Exception("参数 a,b 不可出现负数")
    return a + b


print(sum(1,2))
print(sum(-1,2))