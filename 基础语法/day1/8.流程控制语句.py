if True : print("是正的哦")
if False : print("你是看不到我的")
print("搞起来") if False else print("搞搞")

# 如果想通过条件控制语句，来控制一块代码 这个时候在if后头跟上代码块
# 什么是代码块？
# 代码块中保存着一组代码，同一个代码块的代码要么都执行要么都不执行
# pyton是缩进严格的语言，代码块已缩进开始，恢复到之前的缩进级别时结束（官方推荐4个空格，python中的缩进必须严格统一）
if True :
    print("代码块1")
    print("代码块2")

if 10 > 20 :
    print("10大于20")
else:
    print("10不大于20")

if 10 < 20 < 30:
    print("10小于20并且20小于30")
else:
    print("胡说")

if 10 > 20 : 
    print("10大于20")
elif 10 < 20:
    print("10小于20")    



