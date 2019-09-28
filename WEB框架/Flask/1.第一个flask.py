# 1.导入Flask扩展
from flask import Flask,render_template

# 2.创建Flask应用程序
# 传入__name__,是为了确认资源所在路径
app = Flask(__name__)

# 3.定义路由即试图函数
# Flask中定义路由是通过装饰器实现
@app.route("/")
def hello():
    return "hello flask."

# 返回视图需要导入 render_template
@app.route("/view")
def helloView():
    return render_template("hello.html")

# 4.启动程序    
if __name__ == "__main__":
    # flask会启动一个简易的服务器，用于测试
    app.run()