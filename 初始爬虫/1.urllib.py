from urllib.request import urlopen

# 打开统一资源定位地址 url，可以是一个字符串或一个 Request 对象。
response = urlopen("http://bing.com")
print(response.closed)
with response:
    print(type(response))
    print(response.status,response.reason) # 状态码
    print(response.geturl()) # 获取正在的url
    print(response.info()) # headers
    print(response.read()) # 读取内容
print(response.closed)


