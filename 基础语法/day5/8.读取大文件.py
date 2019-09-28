file_name = "test2.txt"
try:
    with open(file_name,encoding="utf-8") as file_obj:
        # 调用 read 默认会读取所有内容到内存中
        # read中可以接受一个size参数接收要读取的数量；默认值 -1
        # 如果读取到字符末尾没有内容会返回空字符穿 ''
        print(file_obj.read(10))
        print(file_obj.read(10))
except FileNotFoundError:
    print(f"{file_name} 文件不存在")

print("------------------每次读取指定数量----------------------------")

try:
    with open(file_name,encoding="utf-8") as file_obj:
        lin = file_obj.read(10)
        while lin:
            lin = file_obj.read(10)
            print(lin)
except FileNotFoundError:
    print(f"{file_name} 文件不存在")


print("-------------------每次读取一行-------------------------------")

try:
    with open(file_name,encoding="utf-8") as file_obj:
        lin = file_obj.readline()
        while lin:
            lin = file_obj.readline()
            print(lin)
except FileNotFoundError:
    print(f"{file_name} 文件不存在")    

print("-------------------readlines-------------------------------")
try:
    with open(file_name,encoding="utf-8") as file_obj:
        print(file_obj.readlines())
except FileNotFoundError:
    print(f"{file_name} 文件不存在")    

print("-------------------直接遍历文件对象----------------------------")
try:
    with open(file_name,encoding="utf-8") as file_obj:
        for item in file_obj:
            print(item)
except FileNotFoundError:
    print(f"{file_name} 文件不存在")    