# while语句
forSize = 10
while forSize > 0 :
    print("while",forSize)
    forSize -= 1

print("-----------------------------------------")

row = 5
col = 10
while row > 0 :
    row -= 1
    tmpCol = col
    while tmpCol > 0 :
        tmpCol -= 1
        print("*",end="")
    print()

print("-----------------------------------------") 

row = 10
while row > 0 :
    row -= 1
    if row == 5:
        print("row == 5 跳出循环",row)
    if row % 2 == 0:
        print("偶数 continue",row)
        continue    
    
print("-----------------------------------------") 

# for循环
for item in "python" :
    print("当前字母:",item)

print("-----------------------------------------") 

# 遍历一个指定次数的for
for index in range(1,10) :
    print("index",index)    

print("-----------------------------------------") 

# 获取for的下标和值
for index,item in enumerate(range(10,20)) :
    print(index,item)    