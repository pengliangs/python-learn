# 包（package）
# 包也是一个模块
# 普通的模块是一个py文件。而包是一个文件夹
#   包中必须要一个 __init__.py文件,这个文件中可以包含主要的内容
from hello import a,b

print(a.a,b.b)

# __pycache__ 是python的模块缓存文件，避免重复编译，提高程序运行的性能