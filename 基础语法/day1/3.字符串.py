
# 字符串
# 转译符: \
# 可以使用 单引号/双引号表示
msg = "锄禾\"日当午\"，汗滴禾下土，"
print(msg)
msg = '谁知盘中餐，\
粒粒皆辛苦'
print(msg)
# 三重引号: 可以换行及保留字符换行格式
msg = '''锄禾日当午，
汗滴禾下土，
'''
print(msg)

msg = """谁知"盘中餐"，
粒粒皆辛苦
"""
print(msg)

# 字符串只能和字符串进行拼接
p_str = "abc" + "def"
#p_str = "abc" + "def" + 123
print(p_str)

# 站位符的使用
# %s 在字符串中表示任意字符
# %f 浮点数占位符
# %d 整数占位符

# %s 在字符串中表示任意字符
p_str = "你好 %s"%123
print(p_str)
p_str = "你好 %s 我是 %s"%("大佬","帅哥")
print(p_str)

# %3.5s 传入字符串在3-5个字符之间
p_str = "abcd %3.5s"%"efghyjk"
print(p_str)

p_str = "abcd %.2f"%12.221554
print(p_str)

p_str = "abcd %d"%12.221554
print(p_str)

# 格式化字符串嵌入变量
format_str = f"hello {p_str}"
print(format_str)

# 字符串复制
# python中如果字符串 乘以 数量 解析器会将字符串重复指定的次数并返回
a = "a"
a *= 20
print(a)

