operationNumber = int(input("""欢迎来到 python 员工管理系统
1.查看员工列表
2.添加员工
3.删除员工
4.退出
"""))

staff_list = ["张三","李四","王五","赵六"]

if operationNumber == 1 :
    for index,staff in enumerate(staff_list) :
        print(index,staff)
elif operationNumber == 2 :
    username = input("请输入员工名字：")
    staff_list.append(username)
    print("添加成功,当前员工列表")
    for index,staff in enumerate(staff_list) :
        print(index,staff)
elif operationNumber == 3:
    for index,staff in enumerate(staff_list) :
        print(index,staff)
    staff_list.pop(int(input("请输入对应编号进行删除：")))   
    for index,staff in enumerate(staff_list) :
        print(index,staff)
elif operationNumber == 4 :
    print("exit")
else :
    print("输入有误,系统异常退出")
            