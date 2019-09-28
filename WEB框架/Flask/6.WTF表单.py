
from flask import Flask,render_template,request,flash
# 导入 wtf 扩展表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要字段
from wtforms import SubmitField,StringField,PasswordField
# 导入 wtf 扩展，表单验证器
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
# 闪现消息秘钥
app.secret_key = "flash_secret_key"

# 使用 WTF 实现表单
# 需要安装 flask-wtf 模块 pip instal flask-wtf
# 然后自定义一个自定义表单类

class RegisterForm(FlaskForm):
    username = StringField("用户名:",validators=[DataRequired()])
    password = PasswordField("密码:",validators=[DataRequired()])
    passwordTwo = PasswordField("确认密码:",validators=[DataRequired(),EqualTo("password","两次密码输入不一致")])
    submit = SubmitField("提交")

@app.route("/",methods={"GET","POST"})
def register():
    form= RegisterForm()
    if request.method == "POST":
        # 表单提交会有一个跨站 SCRF 错误
        # 在模板表单中添加 {{ form.csrf_token() }}
        if form.validate_on_submit():
            return "success"
        else:
            flash("参数有误")
            
    return render_template("wtf_form.html",form=form)



if __name__ == "__main__":
    app.run()