from flask import Flask,render_template,request,flash

app = Flask(__name__)

"""
给模板发送消息，需要引入flash组件
然后使用flash发送消息，在模板中遍历获取消息

RuntimeError: The session is unavailable because no secret key was set.  
Set the secret_key on the application to something unique and secret.

flash -> 需要对内容加密。因此需要设置 secret_key,做加密消息的混淆

"""
app.secret_key = "flash_secret_key"

@app.route("/",methods={"GET","POST"})
def flash_test():
    # 判断请求方式
    if request.method == "POST":
        # 获取请求参数
        username = request.form.get("username")
        password = request.form.get("password")
        passwordTwo = request.form.get("passwordTwo")
        # 验证参数
        if not all([username,password,passwordTwo]):
            flash(f"参数不完整 username:{username}、password:{password}、passwordTwo:{passwordTwo}")
        elif password != passwordTwo:    
            flash(f"两次输入密码不一致 password:{password}、passwordTwo:{passwordTwo}")
        else:
            return "success"


    return render_template("flash_form.html")


if __name__ == "__main__":
    app.run()