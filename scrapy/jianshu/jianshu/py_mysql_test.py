import pymysql

# 开启连接
db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="jianshu")
# 所有操作都需要通过游标执行
cursor = db.cursor()
try:
    insert_sql = "INSERT INTO `jianshu_article_base_info` (`author_nickname`,`author_avatar`,`title`)\
     VALUES (%s, %s, %s)"
    cursor.execute(insert_sql,("作者昵称","作者头像","标题"))
    db.commit()
    # 查询
    select_sql = "SELECT * FROM `jianshu_article_base_info`"
    count = cursor.execute(select_sql)
    print("COUNT:",count)
    for row in cursor.fetchall():
        print(row)
except:
    print("执行SQL异常")
    db.rollback()
finally:
    cursor.close()

