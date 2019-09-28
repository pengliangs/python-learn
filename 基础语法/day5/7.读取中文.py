# 调用open() 来打开一个文件，可以将文件分为两种类型
# 纯文本:使用 utf-8等编码的文本文件
# 二进制文件：图片，mp3等
# open() 打开文件是，默认是以文本文件打开
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 52: illegal multibyte sequence
# open() 默认值编码 None,所以中文需要手动指定编码
file_name = "test2.txt"
try:
    with open(file_name,encoding="utf-8") as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f"{file_name} 文件不存在")