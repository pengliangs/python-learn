# 文件（file）
# 使用 python 对文件的操作
# 1.打开文件 -> 2.对文件 读/写 操作 -> 3.关闭文件

# 使用 open 函数打开一个文件
file_name = "test.txt"
file_obj = open(file_name)
print(file_obj)

# 读取文件内容
content = file_obj.read()
print(content)

# 关闭文件
file_obj.close()

print("-----------with as 语句----------------------")
# with ... as 语句
# 自动帮助我们关闭文件流
try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f"{file_name} 文件不存在")