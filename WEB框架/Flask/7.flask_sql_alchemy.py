"""
# Flask-SQLAlchemy扩展
* SQLAlchemy 实际上是对数据库的抽象，让开发者不用直接和 SQL 语句打交道，而是通过 python 对象来操作数据库
* SQLAlchmey 是一个关系型数据库框架，它提供了高层的ORM和底层的原生数据库操作。

# 安装 flask-sqlalchemy
pip install flask-sqlalchemy

# 如果连接的是mysql，需要安装mysqldb
pip install flask-mysqldb

# 使用 Flask-SQLAlchemy管理数据库
在Flask-SQLAlchemy中，数据库使用URL指定，程序使用数据库必须保存到Flask配置对象中 SQLALCHEMY_DATABASE_URI 键中

# Flask的数据库设置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysql@127.0.0.1:3306/test"

# 官网
https://flask-sqlalchemy.palletsprojects.com/en/2.x/
http://www.pythondoc.com/flask-sqlalchemy/index.html
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/test'

db = SQLAlchemy(app)

@app.route("/")
def index():
    return "success"


if __name__ == "__main__":
    app.run(debug=True)

