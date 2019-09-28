# request 可以用于获取请求参数信息
from flask import Flask,render_template,request

app = Flask(__name__)

'''
实现一个简单的注册请求
'''
@app.route("/",methods={"GET","POST"})
def register():
    # 判断请求方式
    if request.method == "POST":
        # 获取请求参数
        username = request.form.get("username")
        password = request.form.get("password")
        passwordTwo = request.form.get("passwordTwo")
        # 验证参数
        if not all([username,password,passwordTwo]):
            return f"参数不完整 username:{username}、password:{password}、passwordTwo:{passwordTwo}"
        elif password != passwordTwo:    
            return f"两次输入密码不一致 password:{password}、passwordTwo:{passwordTwo}"
            
        return "success"
    return render_template("form.html")


if __name__ == "__main__":
    app.run()