virtualenv 是一个virtual environment builder for python, 可以简单理解为python工程的虚拟机。

1. 创建独立的python开发环境，不同开发环境相互独立，互不影响。

2. 允许不同的python开发环境使用不同的组件及版本。

# 安装虚拟环境 （virtualenv）

[参考文档](https://www.liaoxuefeng.com/wiki/1016959663602400/1019273143120480)

* 检查是否已安装 virtualenv

```
$ virtualenv --version
```

* 安装

```
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper # 这是对virtualenv的封装版本，一定要在virtualenv后安装 
```

* 切换到对应的目录创建一个虚拟环境

```
$ virtualenv flask_py
```

win步骤是一样的,我的开发环境是win10

直接切换进入虚拟环境，执行 pip 安装后的包全在当前虚拟环境

* WIN10 安装Flask

```
# 启动虚拟环境，执行对应虚拟环境下的Script包中的 `activate` 命令; 退出虚拟环境执行 `deactivate`
> activate

# 安装flask,如果要指定版本，使用 ==版本号
> pip install flask

# 检查是否安装成功
> pip list
# 进入交互模式
> python
# 导入flask模块，如果没有异常代表安装成功
>>> from flask import Flask
```

安装成功后在对应虚拟环境下的 `Lib\site-packages` 下可以看到多了一个 `flask`


# requirements 文件

python 项目中必须包含一个 `requirements.txt` 文件，用于记录所有依赖包及其精确版本号，以便在新的环境中进行部署

在虚拟环境中使用下面命令将当前虚拟环境中的依赖以及版本号生成到文件中：

```
$ pip freeze > requirements.txt
```

当需要创建当前虚拟环境的完全副本，执行如下命令

```
$ pip install -r requirements.txt
```

这个跟java中的 maven, node中的 package.json 同理

