# 模块 (module)
# 模块化将一个完整的程序分解为一个一个的小模块
#   通过模块组合，来搭建出一个完整的程序
# 不采用模块化，统一将所有的代码编写到一个文件
# 采用模块化，将程序分别编写到多个文件
# 模块化有点：便于开发维护、可重用
# 在python中一个 py 文件就是一个模块，要想创建模块实际上就是创建一个py文件
# 注意：模块名要符合标识符规范

# 在一个模块中引入外部模块
# import 模块名称 （模块名称就是python文件名字，注意不要py）
# import 可以在任何位置引入，但是一般我们都放在头部
#   > 引用同一个模块多次，但是模块实例只会创建一个
# import hello_module
# import hello_module
# import hello_module

# 如果觉得模块名称太长了这个时候可以使用 as 关键字 后面跟别名
import hello_module as hm
print(hm)
# __name__ 获取模块名称
print(hm.__name__)

