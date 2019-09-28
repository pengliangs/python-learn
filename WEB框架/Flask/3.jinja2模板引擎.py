from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    # 传入模板参数
    name = "jinja2"
    my_list = [1,2,3,4,5,6]
    my_dict = {
        "name":"张三",
        "age":18
    }
    return render_template("jinja2.html",name=name,my_list=my_list,my_dict=my_dict)


if __name__ == "__main__":
    app.run()