from flask import Flask,flash,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "flash_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@120.78.87.3:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 数据库模型,需要继承 db.Model
class UserBaseInfo(db.Model):
    # 定义标明
    __tablename__ = "user_base_info"
    # 定义字段
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(16),unique = True)
    age = db.Column(db.Integer)



@app.route("/",methods={"GET"})
def index():
    userList = UserBaseInfo.query.order_by(UserBaseInfo.id.desc()).all()
    return render_template("CRUD.html",userList=userList)

@app.route("/add", methods = {"POST"})
def addUser():
    param = {"username":request.form.get("username"),"age":request.form.get("age")}
    user_base_info = UserBaseInfo(**param)
    db.session.add(user_base_info)
    db.session.commit()
    # 重定向
    # redirect 重定向到需要进入 网络/路由地址
    # url_for 需要出入视图函数名称，返回该视图对应的路由地址
    return redirect(url_for("index"))

@app.route("/delete/<int:u_id>", methods = {"GET","POST"})
def delteUser(u_id):
    user = UserBaseInfo.query.get(u_id)
    if user: 
        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            flash("删除失败")
    else:
         flash("未找到用户信息")
  
    return redirect(url_for("index"))


if __name__ == "__main__":
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # 添加初始化数据
    user_base_infos = [
        UserBaseInfo(username="张三",age=18),
        UserBaseInfo(username="李四",age=28), 
        UserBaseInfo(username="王五",age=38),
        UserBaseInfo(username="赵六",age=48), 
    ]
    db.session.add_all(user_base_infos)
    db.session.commit()
    app.run(debug=True)

