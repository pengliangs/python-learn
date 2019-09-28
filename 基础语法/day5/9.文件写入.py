
file_name = "test3.txt"

# io.UnsupportedOperation: not writable
# 使用 open() 打开文件时必须指定所要做的操作（读取、写入、追加）
# 如果不指定，默认是读取文件；读取的时候不能写入
# r：读取文件
# w: 写入文件，如果文件不存在创建文件，如果文件存在新的写入会替换源文件所有内容,但是调用 write写入可多出写入并追加到最后
# a: 追加内容，如果文件不存在创建文件，如果文件存在新的追加到源文件内容后面
# x: 创建文件，不存在创建，存在异常
# + 操作增加功能
# r+: 读/写，文件不存在会报错
# w+: 写/读
# a+: 写/读
with open(file_name,mode="w",encoding="utf-8") as file_obj:
    # write() 向文件中写入内容,返回写入长度
    file_obj.write("这是我写入的1\n")
    file_obj.write("这是我写入的2")