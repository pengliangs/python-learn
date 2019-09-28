file_name = "D:/周杰伦 - 说好不哭（with 五月天阿信）.flac"
# t: 读取文本文件
# b：读取二进制文件
# tell() 获取当前读取到的位置
# seek() 可以修改当前修改位置
#     参数一：要切换的位置
#     参数二：计算位置方式
#        默认：0 从头开始计算、1 当前位置计算、2 从最后位置开始计算
with open(file_name,"rb") as file_obj:
    with open("C:/说好不哭.flac","wb") as new_file_obj:
        # 读取二进制文件
        read_size = 1024 * 100
        file_content = file_obj.read(read_size)

        while file_content: 
            print("当前读取到",new_file_obj.tell())
            # 写入文件
            new_file_obj.write(file_content)
            file_content = file_obj.read(read_size)
        