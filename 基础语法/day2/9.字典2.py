print("> 删除字典key-value")
a = {"name":"张三","age":18,"sex":1}
del a["name"] # 删除不存在key异常
print(a)


print("> popitem() 随机删除字典key-value,一般都是删除最后一个；返回删除的key-value")
a = {"name":"张三","age":18,"sex":1}
print(a,a.popitem()) # 删除空字典异常


print("> pop() 根据key删除字典中的元素,返回删除后的value")
# 删除不存在key会异常，如果指定默认值则直接返回默认值
a = {"name":"张三","age":18,"sex":1}
print(a.pop("name"),a)  
print(a.pop("name2","默认值"),a)  


# 清空字典 clear
a.clear()
print(a)

print("> 浅拷贝copy")
a = {"name":"张三","age":18,"sex":1}
b = a.copy()
b["name"] = "李四"
print(a,b)
print(id(a),id(b))

user_info = {
    "name":"张三",
    "user":{
        "name":"扎扎"
    }
}

user_info_two = user_info.copy()
user_info_two["user"]["name"] = "渣渣"
print(user_info_two,"-",user_info_two)


