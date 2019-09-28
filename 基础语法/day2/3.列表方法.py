usernames = ["张三","李四","王五","赵六"]

# 向列表末尾添加一个新的元素
usernames.append("append")
print(usernames)

# 向列表置顶位置插入元素
usernames.insert(2,"insert")
print(usernames)

# 使用新的序列来扩展，跟 + 效果一样
usernames.extend([1,2,3])
print(usernames)

# 根据索引删除并返回删除元素
print(usernames.pop(0),usernames)

# 弹出列表最后一个元素
print(usernames.pop(),usernames)

# 删除指定值删除,如果存在重复元素删除第一个;不存在异常
usernames.remove("王五")
print(usernames)

# 列表反正
usernames.reverse()
print(usernames)

# 清空序列
usernames.clear()
print(usernames)


numbers = [2,43,54,21,34,78,23,12,4,67,87,21]

#排序 升序
numbers.sort()
print(numbers)

#排序 降序
numbers.sort(reverse=True)
print(numbers)