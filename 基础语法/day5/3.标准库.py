# 全局标准库
# https://docs.python.org/zh-cn/3/py-modindex.html

# sys 模块，提供了一些变量和函数，可以获取到python解析器的信息；通过函数来操作解析器
import sys
# pprint 模块或可以对输出结果格式化
import pprint
# os 模块让我们可以对操作系统进行访问
import os

# sys.argv 执行代码命令行中所包含的参数
print(sys.argv)
# D:\github\python-learn>D:/devSoft/python/python3.7.4/python.exe d:/github/python-learn/基础语法/day5/3.标准库.py a b c
# ['d:/github/python-learn/基础语法/day5/3.标准库.py', 'a', 'b', 'c']

# sys.modules 获取当前程序中所有模块字典
pprint.pprint(sys.modules)

# sys.path 模块搜索路径
pprint.pprint(sys.path)

# sys.platform 运行平台
print(sys.platform)

# sys.exit 退出
# sys.exit("exit")
# print("结束了么")


# os.environ 获取系统的环境变量
print(os.environ)

# os.system 执行操作系统命令
# os.system("dir")