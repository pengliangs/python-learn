from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/test'

db = SQLAlchemy(app)

# 数据库模型,需要继承 db.Model
class UserBaseInfo(db.Model):
    # 定义标明
    __tablename__ = ""
    # 定义字段
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(16),unique = True)
    age = db.Column(db.Integer)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

@app.route("/")
def index():
    return "success"


if __name__ == "__main__":
    app.run(debug=True)

