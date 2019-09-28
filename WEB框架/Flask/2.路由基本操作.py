from flask import Flask

app = Flask(__name__)

# 路由默认GET,其他类型使用methods参数限定请求类型
@app.route("/",methods={'GET','POST'})
def hello():
    return "hello flask"

# 带参数的路由
# 在路由中使用 <> 包裹的参数，会被路由解析;注意函数参数列表名称必须和<>中指定的参数名相同


@app.route("/print/<name>")
def printName(name):
    return "你好,我是 %s"%name

# 参数类型，默认是字符串
# 如果要指定参数格式，则在<>变量名前面加上 数据类型冒号 如 <int:a>
# 指定了数据类型，路由会帮我们强转为对应类型，转换成功则匹配否则不匹配
@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
    return "计算结果:%s"%(a+b)

if __name__ == "__main__":
    app.run()    