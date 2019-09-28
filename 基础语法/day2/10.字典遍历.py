# 遍历字典
# keys() 返回字典所有key
user_info = {
    "name":"张三",
    "age":18,
    "sex":"男"
}

for item in user_info.keys() :
    print("key:",item,",value:",user_info[item])

print("--------------------------------------------------")
# values()
for item in user_info.values() :
    print("value:",item)

print("--------------------------------------------------")
# items()
for item in user_info.items() :
    print("item:",item)

print("--------------------------------------------------")
# items()
for k,v in user_info.items() :
    print("key:",k,",value:",v)    