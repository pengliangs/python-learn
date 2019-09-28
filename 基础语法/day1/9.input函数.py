# 用户输入 “admin” 打印 “欢迎管理员光临” 如果是 “user” 打印 “欢迎光临” 否则不做处理
username = input("请输入您的用户名称：")
if username == "admin" : 
    print("欢迎管理员光临")
elif username == "user":
    print("欢迎光临")
   