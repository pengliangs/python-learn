from urllib.request import urlopen,Request

url = "http://bing.com";
# 请求对象
req = Request(url,headers={
    # 用户头信息，模拟一个浏览器
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/77.0.3865.90 Safari/537.36"
})

# 打开统一资源定位地址 url，可以是一个字符串或一个 Request 对象。
response = urlopen(req)

with response:
    print(type(response))
    print(response.status,response.reason) # 状态码
    print(response.geturl()) # 获取正在的url
    print(response.info()) # headers
    print(response.read()) # 读取内容
print(response.closed)


